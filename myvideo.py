import cv2
import numpy as np

cap = cv2.VideoCapture('videos/video1.mp4')
while True:
    success, img = cap.read()

    img = cv2.GaussianBlur(img, (15, 15), 0)  # размытие (?)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # ЧБ видео
    img = cv2.Canny(img, 50, 50)  # контур картинки

    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
