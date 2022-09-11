import tkinter
from PIL import Image, ImageTk # pip install PIL
root = tkinter.Tk()

# создаем рабочую область
frame = tkinter.Frame(root)
frame.grid()

width = root.winfo_width() # Ширина окна
height = root.winfo_height() # Высота окна
canvas = tkinter.Canvas(root, height=550, width=540)

#https://intellij-support.jetbrains.com/hc/en-us/community/posts/206732719-How-to-import-jpg-png-into-a-pycharm-

img = Image.open('img/bg1.png') # Открываем картинку
img = img.resize((500, 500)) # Изменяем размер картинки
img_tk = ImageTk.PhotoImage(img) # Создаём PhotoImage
canvas.create_image(0,0 ,anchor="nw", image=img_tk) # Рисуем картинку
canvas.grid(row=2,column=1)
root.mainloop()
