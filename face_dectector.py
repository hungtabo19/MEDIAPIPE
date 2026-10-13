#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp

# =========================================
# 🧩 MediaPipe Face Detection 초기화
# =========================================
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# model_selection: 0 = 2미터 이내 근거리 대면(웹캠용), 1 = 5미터 이내 원거리 전신용
face_detection = mp_face_detection.FaceDetection(
    model_selection=0, 
    min_detection_confidence=0.5
)

# =========================================
# 📸 카메라 연결
# =========================================
# cv2.CAP_DSHOW는 윈도우 환경에서 카메라를 렉 없이 즉시 실행하도록 도와줍니다.
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 카메라 해상도 설정 (기본 화질)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("📷 얼굴 인식 시작 — ESC를 눌러 종료합니다.")

# =========================================
# 🎞️ 실시간 얼굴 인식 루프
# =========================================
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("⚠️ 영상을 읽지 못했습니다. 카메라 연결을 확인하세요.")
        break

    # 웹캠 화면을 거울 모드(좌우 반전)로 변경
    image = cv2.flip(image, 1)

    # MediaPipe 처리를 위해 BGR에서 RGB로 색상 채널 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 얼굴 검출 수행
    results = face_detection.process(image_rgb)

    # 👤 감지된 얼굴에 사각형 상자 및 주요 특징점 그리기
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

    # 결과 화면 표시
    cv2.imshow('👤 MediaPipe Face Detector', image)

    # ESC 키를 누르면 루프 종료 (1ms 대기하여 부드러운 재생 속도 유지)
    if cv2.waitKey(1) & 0xFF == 27:
        print("👋 프로그램을 종료합니다.")
        break

# =========================================
# 🔚 자원 해제 및 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()
