# 저강도 기능 움직임 메뉴판

웨이트트레이닝이나 크로스핏의 일반적인 근력·심폐 동작을 제외하고, 집에서 가볍게 수행할 수 있는 기능 움직임 22가지를 정리한 개인용 메뉴판입니다.

- 골반을 세우는 감각과 장좌 자세 준비
- 햄스트링 및 고관절 가동성
- 척추 분절과 흉추 회전
- 발·발목 기능과 균형
- 견갑·목 조절
- 측면·회전 저항과 저강도 힘줄 적응

각 카드에는 권장 반복수 또는 유지 시간, 필요한 경우 한 줄짜리 핵심 큐가 포함됩니다. 특정 진단을 교정하거나 치료하기 위한 처방이 아니며, 날카로운 통증·저림·힘 빠짐이 생기면 중단해야 합니다.

## 웹과 PDF

- GitHub Pages: 저장소의 `docs/`에서 제공
- 출력용 PDF: `output/pdf/functional_movement_menu.pdf`
- 최신 생성 스크립트: `make_functional_menu_v2.py`

## 재생성

Python과 `reportlab`, `Pillow`가 필요합니다.

```bash
python3 make_functional_menu_v2.py
```

## 매일 Telegram 루틴

`.github/workflows/daily-telegram-routine.yml`이 매일 한국 시각 낮 12시에 실행됩니다. 날짜를 기준으로 다섯 영역에서 한 동작씩 골라 약 10분 분량의 루틴을 만들고, 동작 그림과 권장량을 Telegram 앨범으로 전송합니다.

저장소 Actions Secrets에는 다음 값이 필요합니다.

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

로컬에서 조합만 확인하려면 다음을 실행합니다.

```bash
python3 scripts/send_daily_routine.py --dry-run
```

## 참고 원칙

동작 구성과 안전 문구는 다음 자료의 보수적인 원칙을 참고했습니다.

- [APTA Orthopedics: Low Back Pain Clinical Practice Guideline](https://www.orthopt.org/content/s/interventions-for-the-management-of-acute-and-chronic-low-back-pain-revision-2021)
- [ChoosePT: 30-Minute Home Stretching Program](https://www.choosept.com/health-tips/30-minute-home-stretching-program)
- [ACSM: Exercise for the Prevention and Treatment of Hypertension](https://acsm.org/exercise-for-the-prevention-and-treatment-of-hypertension/)

## 글꼴 및 이미지

- 글꼴: [Pretendard](https://github.com/orioncactus/pretendard), SIL Open Font License 1.1
- 동작 이미지는 이 프로젝트를 위해 생성한 임상 안내도 스타일의 일러스트입니다.
