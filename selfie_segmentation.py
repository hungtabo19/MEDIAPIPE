#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import mediapipe as mp

# =========================================
# 🧩 Mediapipe Selfie Segmentation 초기화
# =========================================
mp_selfie = mp.solutions.selfie_segmentation

# Sử dụng model_selection=0 để chạy mượt mà và load nhanh hơn trên CPU/Camera thường
segmenter = mp_selfie.SelfieSegmentation(model_selection=0)

# =========================================
# 📸 Kết nối Camera (Đã sửa ở đây)
# =========================================
# cv2.CAP_DSHOW giúp Windows nhận diện và kích hoạt camera ngay lập tức, tránh bị treo
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Cấu hình độ phân giải camera chuẩn (Có thể bỏ qua nếu camera tự nhận tốt)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("📷 Selfie Segmentation 시작 — ESC를 눌러 종료합니다.")

# =========================================
# 🎞️ 실시간 배경 분리 루프
# =========================================
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("⚠️ 영상이 끝났거나 프레임을 읽지 못했습니다. (카메라 sử dụng đang bị chiếm hoặc chưa kết nối)")
        break

    # 좌우 반전 (셀카 모드)
    frame = cv2.flip(frame, 1)

    # BGR → RGB 변환
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 배경 분리 수행
    result = segmenter.process(rgb)

    # segmentation mask 생성
    mask = (result.segmentation_mask > 0.5).astype(np.uint8)

    # 배경 블러 생성 (Làm mờ nền hậu cảnh)
    blur = cv2.GaussianBlur(frame, (31, 31), 0)

    # 전경/배경 합성
    output = frame * mask[..., None] + blur * (1 - mask[..., None])
    output = output.astype(np.uint8)

    # 화면에 맞게 크기 조정
    h, w = output.shape[:2]
    if h > 720:
        output = cv2.resize(output, (int(w * 720 / h), 720))

    # 결과 화면 표시
    cv2.imshow("Selfie Segmentation (ESC to quit)", output)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        print("👋 종료합니다.")
        break

# =========================================
# 🔚 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()
