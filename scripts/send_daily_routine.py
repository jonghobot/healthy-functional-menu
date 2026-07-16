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
    3: ("벽에 기대 다리 펴고 앉기", "20~30초 × 2", "docs/assets/movements/p1_03.png"),
    4: ("수건 받치고 다리 펴고 앉기", "20~30초 × 2", "docs/assets/movements/p1_04.png"),
    5: ("누워서 한쪽 무릎 펴기", "좌우 6~10회", "docs/assets/movements/p1_05.png"),
    6: ("앉아서 뒤꿈치 바닥 누르기", "10~20초 × 2", "docs/assets/movements/p1_06.png"),
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
    23: ("엎드려 등 뒤로 호흡하기", "5호흡 × 2", "docs/assets/movements/p3_01.png"),
    24: ("옆으로 누워 옆구리 호흡하기", "좌우 5호흡", "docs/assets/movements/p3_02.png"),
    25: ("아기 자세에서 손 옆으로 걷기", "좌우 20~30초 × 2", "docs/assets/movements/p3_03.png"),
    26: ("네발 자세에서 팔 겨드랑이로 넣기", "좌우 5~8회", "docs/assets/movements/p3_04.png"),
    27: ("네발 자세에서 한 팔 천장으로 열기", "좌우 5~8회", "docs/assets/movements/p3_05.png"),
    28: ("폼롤러에 등 대고 가슴 열기", "5~8회", "docs/assets/movements/p3_06.png"),
    29: ("벽 짚고 옆구리 늘리기", "좌우 20~30초 × 2", "docs/assets/movements/p3_07.png"),
    30: ("의자에 앉아 가슴 돌리기", "좌우 5~8회", "docs/assets/movements/p3_08.png"),
    31: ("벽에 기대 등 말아 내려가기", "5~8회", "docs/assets/movements/p3_09.png"),
    32: ("누워서 척추 말아 엉덩이 들기", "5~8회", "docs/assets/movements/p3_10.png"),
    33: ("네발 자세에서 몸 앞뒤로 흔들기", "8~10회", "docs/assets/movements/p3_11.png"),
    34: ("엎드려 발 좌우로 벌리기", "좌우 왕복 5~8회", "docs/assets/movements/p4_01.png"),
    35: ("누워서 4자 스트레칭", "좌우 20~30초 × 2", "docs/assets/movements/p4_02.png"),
    36: ("누워서 한쪽 다리 옆으로 열기", "좌우 6~10회", "docs/assets/movements/p4_03.png"),
    37: ("개구리 자세에서 엉덩이 뒤로 빼기", "6~10회", "docs/assets/movements/p4_04.png"),
    38: ("누워서 무릎 바깥으로 밀고 버티기", "10~20초 × 2", "docs/assets/movements/p4_05.png"),
    39: ("옆으로 누워 무릎 벌리고 버티기", "좌우 10~20초 × 2", "docs/assets/movements/p4_06.png"),
    40: ("의자 잡고 고관절 원 그리기", "좌우 방향별 3~5회", "docs/assets/movements/p4_07.png"),
    41: ("누워서 한쪽 무릎 가슴으로 당기기", "좌우 20~30초 × 2", "docs/assets/movements/p4_08.png"),
    42: ("뒤꿈치 받치고 무릎 편하게 펴기", "30~60초 × 2", "docs/assets/movements/p4_09.png"),
    43: ("수건 누르며 허벅지 힘주기", "5초 × 8회", "docs/assets/movements/p4_10.png"),
    44: ("의자에서 무릎 천천히 펴고 굽기", "좌우 6~10회", "docs/assets/movements/p4_11.png"),
    45: ("엄지와 나머지 발가락 따로 들기", "각 5~8회", "docs/assets/movements/p5_01.png"),
    46: ("앉아서 발목 원 그리기", "좌우 방향별 5회", "docs/assets/movements/p5_02.png"),
    47: ("발뒤꿈치와 발가락 번갈아 들기", "8~12회", "docs/assets/movements/p5_03.png"),
    48: ("벽 짚고 종아리 늘리기", "좌우 20~30초 × 2", "docs/assets/movements/p5_04.png"),
    49: ("무릎 굽혀 종아리 아래쪽 늘리기", "좌우 20~30초 × 2", "docs/assets/movements/p5_05.png"),
    50: ("발을 일자로 두고 서기", "좌우 앞발 20~30초 × 2", "docs/assets/movements/p5_06.png"),
    51: ("벽 짚고 발로 시계 그리기", "좌우 방향별 3회", "docs/assets/movements/p5_07.png"),
    52: ("쿠션 위에 두 발로 서기", "20~30초 × 2", "docs/assets/movements/p5_08.png"),
    53: ("밴드를 바깥으로 밀고 버티기", "좌우 10~20초 × 2", "docs/assets/movements/p5_09.png"),
    54: ("벽에 기대 발등 들어올리기", "8~12회 × 1~2", "docs/assets/movements/p5_10.png"),
    55: ("벽 짚고 체중 좌우로 옮기기", "좌우 왕복 8~10회", "docs/assets/movements/p5_11.png"),
    56: ("벽에 기대 팔 위아래로 움직이기", "6~10회", "docs/assets/movements/p6_01.png"),
    57: ("벽 짚고 날개뼈 시계 그리기", "방향별 5회", "docs/assets/movements/p6_02.png"),
    58: ("폼롤러 밀며 팔 위로 올리기", "6~10회", "docs/assets/movements/p6_03.png"),
    59: ("문틀 짚고 가슴 앞쪽 늘리기", "좌우 20~30초 × 2", "docs/assets/movements/p6_04.png"),
    60: ("팔을 가슴 앞으로 당겨 늘리기", "좌우 20~30초 × 2", "docs/assets/movements/p6_05.png"),
    61: ("팔 크게 원 그리기", "좌우 방향별 3~5회", "docs/assets/movements/p6_06.png"),
    62: ("손바닥 위로 두고 손목 늘리기", "좌우 20초 × 2", "docs/assets/movements/p6_07.png"),
    63: ("손등 위로 두고 손목 늘리기", "좌우 20초 × 2", "docs/assets/movements/p6_08.png"),
    64: ("팔과 손목 부드럽게 신경 움직이기", "좌우 5~8회", "docs/assets/movements/p6_09.png"),
    65: ("의자에 앉아 목 좌우로 돌리기", "좌우 5~8회", "docs/assets/movements/p6_10.png"),
    66: ("고개 겨드랑이 쪽으로 숙여 늘리기", "좌우 15~20초 × 2", "docs/assets/movements/p6_11.png"),
}

# One choice from each slot keeps every day balanced without tracking user data.
SLOTS = [
    [1, 2, 23, 24, 31],
    [3, 4, 5, 6, 7, 9, 25, 33, 35, 37, 41, 42],
    [8, 10, 11, 32, 34, 36, 38, 39, 40, 43, 44],
    [12, 13, 14, 16, 26, 27, 28, 29, 30, 46, 48, 49, 50, 51, 52, 55],
    [15, 17, 18, 19, 20, 21, 22, 45, 47, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],
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
