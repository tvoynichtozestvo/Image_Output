import cv2
import os
import tkinter as tk
from PIL import ImageTk, Image


class ImageViewer:
    def __init__(self):
        self.img_tk = None  # Сохраняем ссылку на объект ImageTk

        self.root = tk.Tk()
        self.root.title("Загрузить изображение")

        self.button = tk.Button(self.root, text="Показать изображение", command=self.show_image)
        self.button.pack()

    def show_image(self):
        # Проверяем, существует ли файл "images/image1.jpg"
        if os.path.isfile("images/image1.jpg"):
            try:
                # Читаем изображение
                img = cv2.imread("images/image1.jpg", cv2.IMREAD_UNCHANGED)
                # Отражаем изображение по горизонтали
                img = cv2.flip(img, 1)
                # Преобразуем изображение в формат, подходящий для отображения в tkinter
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                self.img_tk = ImageTk.PhotoImage(img)
                # Создаем виджет Label для отображения изображения
                label = tk.Label(self.root, image=self.img_tk)
                label.pack()
            except Exception as e:
                print("Ошибка: ", e)
        else:
            print("Файл не найден")

    def run(self):
        # Запускаем главный цикл обработки событий tkinter
        self.root.mainloop()


# Создаем экземпляр класса ImageViewer и запускаем программу
viewer = ImageViewer()
viewer.run()
