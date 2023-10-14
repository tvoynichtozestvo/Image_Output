import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')  # создание изображения 300 на 300 пикселей, черное, 3 слоя

# RGB - стандартный формат
# BGR - формат в OpenCV

# photo[50:150, 200:280] =   # высота, ширина


# создение квадрата
cv2.rectangle(photo, (80, 80), (100, 100), (150, 50, 100), thickness=cv2.FILLED)

# создание линии:
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (150, 50, 100), thickness=5)

# создание круга:
cv2.circle(photo, (photo.shape[0] // 2, photo.shape[0] // 2), 100, (150, 50, 100), thickness=cv2.FILLED)

# добавление текста
cv2.putText(photo, 'ChtoTakoe', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 30, 0), 2)


cv2.imshow('Photo', photo)  # вывод изображения на экран
cv2.waitKey(0)  # бесконечный показ изображения
