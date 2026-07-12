#!/usr/bin/env python3
"""Choose a balanced 10-minute routine and send it to Telegram as a photo album."""

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]

MOVES = {
    1: ("벽에 다리 올리고 90-90 호흡", "5호흡 × 1~2", "docs/assets/movements/p1_01.png"),
    2: ("누워서 골반 앞뒤로 굴리기", "방향별 5회", "docs/assets/movements/p1_02.png"),
    5: ("누워서 한쪽 무릎 펴기", "좌우 6~10회", "docs/assets/movements/p1_05.png"),
    7: ("엉덩이로 벽 터치하기", "6~10회 × 1~2", "docs/assets/movements/p1_07.png"),
    8: ("반무릎 고관절 앞쪽 스트레칭", "좌우 15~30초 × 2", "docs/assets/movements/p1_08.png"),
    9: ("한쪽 다리 벌리고 엉덩이 뒤로 빼기", "좌우 6~10회", "docs/assets/movements/p1_09.png"),
    10: ("앉아서 90-90 무릎 넘기기", "좌우 왕복 5~8회", "docs/assets/movements/p1_10.png"),
    11: ("누워서 무릎 좌우로 넘기기", "좌우 왕복 5~8회", "docs/assets/movements/p1_11.png"),
    12: ("옆으로 누워 가슴 열기", "좌우 5~8회", "docs/assets/movements/p2_01.png"),
    13: ("캣카우", "5~8회 × 1~2", "docs/assets/movements/p2_02.png"),
    14: ("뒤꿈치 붙이고 무릎 벽에 대기", "좌우 6~10회", "docs/assets/movements/p2_03.png"),
    15: ("발가락 편 채 발 아치 만들기", "5~10초 × 5", "docs/assets/movements/p2_04.png"),
    16: ("벽 짚고 한 발로 서기", "좌우 20~30초 × 2", "docs/assets/movements/p2_05.png"),
    17: ("벽에서 팔 위로 미끄러뜨리기", "6~10회 × 1~2", "docs/assets/movements/p2_06.png"),
    18: ("밴드를 바깥으로 벌리고 버티기", "10~20초 × 2", "docs/assets/movements/p2_07.png"),
    19: ("벽에 기대 턱 당기기", "5~8회 · 각 3초", "docs/assets/movements/p2_08.png"),
    20: ("무릎으로 벽 밀고 버티기", "좌우 10~20초 × 2", "docs/assets/movements/p2_09.png"),
    21: ("팔로프 프레스 버티기", "좌우 10~20초 × 2", "docs/assets/movements/p2_10.png"),
    22: ("벽 짚고 까치발 버티기", "15~30초 × 2", "docs/assets/movements/p2_11.png"),
}

# One choice from each slot keeps every day balanced without tracking user data.
SLOTS = [
    [1, 2],                 # breathing / pelvis reset
    [5, 7, 9],             # hamstring / hinge / inner hip
    [8, 10, 11],           # hip mobility and rotation
    [12, 13, 14, 16],      # spine / ankle / balance
    [15, 17, 18, 19, 20, 21, 22],  # foot / upper body / stability / tendon
]


def choose(date: dt.date) -> list[int]:
    seed = date.toordinal()
    return [slot[(seed + i * 3) % len(slot)] for i, slot in enumerate(SLOTS)]


def captions(date: dt.date, selected: list[int]) -> list[str]:
    result = []
    for index, move_id in enumerate(selected, 1):
        name, dose, _ = MOVES[move_id]
        prefix = f"🌿 {date:%m월 %d일} · 오늘의 10분 움직임\n\n" if index == 1 else ""
        result.append(
            f"{prefix}{index}/5  {name}\n{dose} · 약 2분\n\n"
            "편안한 범위에서 천천히 수행하세요."
        )
    return result


def send_album(token: str, chat_id: str, selected: list[int], text: list[str]) -> None:
    media = []
    command = ["curl", "--fail-with-body", "--silent", "--show-error", "--max-time", "45"]
    for index, (move_id, caption) in enumerate(zip(selected, text)):
        _, _, relative = MOVES[move_id]
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        attach = f"photo{index}"
        command.extend(["-F", f"{attach}=@{path}"])
        media.append({"type": "photo", "media": f"attach://{attach}", "caption": caption})
    command.extend([
        "-F", f"chat_id={chat_id}",
        "-F", f"media={json.dumps(media, ensure_ascii=False)}",
        f"https://api.telegram.org/bot{token}/sendMediaGroup",
    ])
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    response = json.loads(completed.stdout)
    if not response.get("ok"):
        raise RuntimeError(response.get("description", "Telegram API error"))
    print(f"Sent {len(response['result'])} routine images.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--date", help="KST date in YYYY-MM-DD")
    args = parser.parse_args()
    today = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(ZoneInfo("Asia/Seoul")).date()
    selected = choose(today)
    text = captions(today, selected)
    if args.dry_run:
        print(json.dumps({"date": str(today), "moves": [{"id": i, "name": MOVES[i][0], "dose": MOVES[i][1]} for i in selected]}, ensure_ascii=False, indent=2))
        return
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        raise SystemExit("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required")
    send_album(token, chat_id, selected, text)


if __name__ == "__main__":
    main()

