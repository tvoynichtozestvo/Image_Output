import cv2  # библитека для работы с изображенями
import numpy as np  # создаем матрицу с помощью этой библотеки. As - псевдоним. Это библиотека дял численных вычислений.


img = cv2.imread('images/image1.jpg')
new_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# new_img[0:100, 0:150] обрезка фото под определенные величины


# методы для редакирования изображений:

# new_img = cv2.GaussianBlur(img, (129, 129), 0)   # размытие изображения

# new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # картинка в формате чб

# new_img = cv2.Canny(img, 90, 90)  # картинка в 2-ух цветах


kernel = np.ones((5, 5), np.uint8)  # создание матрицы 5 на 5 только с целими числами. Метод увел. обводку
new_img = cv2.dilate(img, kernel, iterations=1)

new_img = cv2.erode(img, kernel, iterations=1)  # уменьшает обводку

cv2.imshow('Result', new_img)

# print(img.shape)

cv2.waitKey(0)


# РАБОТА С ВИДЕО:


# cap = cv2.VideoCapture('videos/video1.mp4')    # если использовать значение 0, то тогда комп. будет счывать инфу из
# камеры. После необходимо спользовать метод cap.set(размер, ширину)

# while True:
#    success, img = cap.read()   # в значение seccess будет помещаться значение t или f, а в значение img будет картинки
#    cv2.imshow('Result', img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
