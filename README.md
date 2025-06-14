# Python CMD — 간단한 커맨드 라인 인터프리터

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Terminal](https://img.shields.io/badge/Terminal-Simple-green)

## 목차
[소개](#소개)
[기능](#기능)
[사용 방법](#사용-방법)

## 소개

Python으로 직접 만든 간단한 커맨드 라인 인터프리터입니다.  
기본적인 `echo`, `date`, `time`, `ipconfig`, `sysinfo`, `random`, `py` 실행 등 여러 명령어를 지원하며,  
터미널의 느낌을 살린 `> ` 프롬프트와 시작 메시지로 구성되어 있습니다.

---

## 기능

| 명령어    | 설명                                   |
| --------- | ------------------------------------ |
| `echo`    | 입력한 내용을 그대로 출력합니다.      |
| `date`    | 현재 날짜를 `YYYY년 MM월 DD일` 형식으로 출력합니다. |
| `time`    | 현재 시간을 `HH:MM:SS` 형식으로 출력합니다.         |
| `random`  | 사용자 지정 범위 내 랜덤 숫자를 생성합니다.          |
| `ipconfig`| 호스트명과 IP 주소를 출력합니다.        |
| `sysinfo` | 시스템 정보(운영체제, 아키텍처, CPU 등)를 출력합니다.  |
| `py`      | 파이썬 코드를 즉석에서 실행합니다.      |
| `cmd`     | 시작 메시지를 다시 출력합니다.         |
| `help`    | 사용 가능한 명령어 목록을 보여줍니다.   |
| `exit`    | 프로그램을 종료합니다.                 |

---

## 사용 방법

1. Python 3.8 이상이 설치되어 있어야 합니다.
2. 코드를 복사하거나 클론한 후, 터미널에서 실행하세요:

```bash
python python_cmd.py
