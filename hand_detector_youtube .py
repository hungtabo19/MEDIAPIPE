#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
import yt_dlp

# =========================================
# 🧩 MediaPipe Hands 초기화
# =========================================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,       # 실시간 동영상 스트림 처리
    max_num_hands=2,              # 최대 감지할 손 개수
    min_detection_confidence=0.5, # 손 감지 최소 신뢰도
    min_tracking_confidence=0.5   # 손 추적 최소 신뢰도
)

# =========================================
# 📺 유튜브 동영상 스트림 연결 설정 (플레이리스트 예외 처리 추가)
# =========================================
# 🟢 재생목록 코드가 포함된 유튜브 링크도 정상 작동합니다.
youtube_url = "https://www.youtube.com/shorts/6aE9mpzu32Y?feature=share" 

print("⏳ 유튜브 동영상 연결 중... 잠시만 기다려주세요.")

# 플레이리스트 주소가 들어와도 단일 영상만 추출하도록 옵션 수정
ydl_opts = {
    'format': 'best[ext=mp4]/best', 
    'quiet': True,
    'no_warnings': True,
    'noplaylist': True,  # 💡 재생목록 전체를 불러오지 않고 현재 영상만 추출하는 옵션 추가
    'extractor_args': {'youtube': {'player_client': ['android', 'web_embedded']}} 
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_url = info_dict.get('url', None)
except Exception as e:
    print(f"❌ 유튜브 동영상 정보를 가져오는 중 오류가 발생했습니다: {e}")
    print("💡 해결 방법: 터미널에 'pip install -U yt-dlp'를 입력하여 라이브러리를 업데이트 하세요.")
    exit()

# OpenCV를 사용하여 유튜브 스트리밍 URL 연결
cap = cv2.VideoCapture(video_url)

# 연결이 정상적으로 수행되었는지 검증
if not cap.isOpened():
    print("❌ OpenCV가 유튜브 비디오 스트림을 열지 못했습니다.")
    exit()

print("📷 유튜브 스트림 시작 — ESC를 눌러 종료합니다.")

# =========================================
# 🎞️ 실시간 손 검출 루프
# =========================================
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("⚠️ 영상이 끝났거나 프레임을 읽지 못했습니다.")
        break

    # MediaPipe 처리를 위해 BGR에서 RGB로 색상 채널 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 손 인식을 위한 프로세싱 수행
    result = hands.process(image_rgb)

    # 🖐️ 손 랜드마크 화면에 그리기
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

    # 화면 크기 자동 조정 (고해상도 영상이 모니터 창 밖으로 잘리는 현상 방지)
    h, w = image.shape[:2]
    if h > 720:
        image = cv2.resize(image, (int(w * 720 / h), 720))

    # 결과 화면 표시
    cv2.imshow('🖐️ MediaPipe Hand Detector (YouTube)', image)

    # ESC 키를 누르면 루프 종료 (1ms 대기하여 부드러운 재생 속도 유지)
    if cv2.waitKey(1) & 0xFF == 27:
        print("👋 프로그램을 종료합니다.")
        break

# =========================================
# 🔚 자원 해제 및 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()
