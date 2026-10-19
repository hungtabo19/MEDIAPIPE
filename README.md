# Python 기반 컴퓨터 비전 프로젝트 (Computer Vision Project)

## 1. 프로젝트 소개

이 프로젝트는 Python을 활용한 컴퓨터 비전(Computer Vision) 및 이미지 처리 기술을 학습하고 실습하기 위한 프로젝트입니다.

OpenCV와 MediaPipe를 활용하여 얼굴 인식, 손 인식, 손 추적 및 셀카 이미지 분할 기능을 구현합니다.

본 프로젝트의 목적은 컴퓨터 비전의 기본 원리를 이해하고, 향후 인공지능(AI), 로봇 및 드론 제어 시스템 개발에 활용할 수 있는 기초 기술을 습득하는 것입니다.

## 2. 프로젝트 구조

```text
project/
│
├── .gitignore
├── face_dectector.py
├── hand_detector.py
├── hand_detector_youtube .py
├── requirements.txt
└── selfie_segmentation.py
```

## 3. 파일 설명

| 파일명 | 설명 |
|---|---|
| `.gitignore` | Git에서 추적하지 않을 파일 및 폴더를 지정합니다. |
| `face_dectector.py` | Python을 사용하여 이미지 또는 영상에서 얼굴을 인식하는 프로그램입니다. |
| `hand_detector.py` | 손을 인식하고 손의 주요 특징점을 검출하는 프로그램입니다. |
| `hand_detector_youtube .py` | 손 인식 및 추적 기능을 실습하기 위한 프로그램입니다. |
| `requirements.txt` | 프로젝트 실행에 필요한 Python 라이브러리 목록을 관리합니다. |
| `selfie_segmentation.py` | 이미지에서 사람을 배경과 분리하는 셀카 이미지 분할 프로그램입니다. |

※ 각 프로그램의 구체적인 기능은 실제 소스 코드를 확인하여 검증해야 합니다.

## 4. 사용 기술

- **Python**: 프로그램 개발을 위한 주요 프로그래밍 언어
- **OpenCV**: 이미지 처리, 영상 분석 및 카메라 제어
- **MediaPipe**: 얼굴 인식, 손 인식 및 이미지 분할
- **NumPy**: 배열 연산 및 수치 데이터 처리(사용하는 경우)

## 5. 개발 환경

- Python이 설치된 컴퓨터
- Visual Studio Code 또는 Python 개발 환경
- 웹캠(실시간 영상 처리를 수행하는 경우)
- `requirements.txt`에 명시된 Python 라이브러리

## 6. 설치 방법

### 6.1. 프로젝트 다운로드

GitHub에서 프로젝트를 다운로드하거나 다음 명령어를 사용하여 저장소를 복제합니다.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

위 명령어에서 저장소 URL과 프로젝트 폴더명을 실제 정보로 변경해야 합니다.

### 6.2. 가상 환경 생성

```bash
python -m venv .venv
```

Windows PowerShell에서 가상 환경을 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

### 6.3. 라이브러리 설치

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 7. 프로그램 실행 방법

각 Python 파일을 개별적으로 실행할 수 있습니다.

**얼굴 인식**

```bash
python face_dectector.py
```

**손 인식**

```bash
python hand_detector.py
```

**손 인식 실습 프로그램**

```bash
python "hand_detector_youtube .py"
```

**셀카 이미지 분할**

```bash
python selfie_segmentation.py
```

※ `hand_detector_youtube .py` 파일명에는 `.py` 앞에 공백이 있습니다. 실제 파일명이 다르다면 해당 파일명에 맞게 실행해야 합니다. 유지보수를 쉽게 하려면 `hand_detector_youtube.py`로 변경하는 것을 권장합니다.

## 8. 주요 활용 분야

- 웹캠을 이용한 실시간 얼굴 인식
- 손과 손가락의 위치 추적
- 손동작 및 제스처 인식
- 이미지와 영상에서 사람과 배경 분리
- 인공지능 기반 객체 추적 시스템 개발
- 로봇 및 드론의 영상 인식 시스템 개발

## 9. 향후 개발 계획

- 얼굴 및 손 인식 정확도 개선
- 손가락 개수 인식 기능 추가
- 실시간 객체 추적 기능 구현
- 카메라 영상과 ESP32 기반 제어 시스템 연동
- 영상 처리 속도 및 시스템 응답 속도 최적화
- 인식 결과를 활용한 로봇 및 드론 제어 연구

## 10. 개발자

**Nguyen Manh Hung**

본 프로젝트는 Python 프로그래밍, 컴퓨터 비전 및 인공지능 기술에 대한 학습과 연구를 목적으로 합니다.

## License

현재 라이선스는 지정되지 않았습니다. 프로젝트를 공개적으로 배포하거나 다른 사람이 코드를 활용할 수 있도록 하려면 적절한 라이선스를 추가해야 합니다.
