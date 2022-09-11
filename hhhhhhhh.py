'''from tkinter import *
#https://younglinux.info/tkinter/canvasmeth
root = Tk()
c = Canvas(width=200, height=200,
           bg='white')
c.pack()

rect = c.create_rectangle(
    80, 80, 120, 120, fill='lightgreen')


def in_focus(event):
    c.itemconfig(rect, fill='green', width=20)#width=20 breite von Rand
    c.coords(rect, 70, 70, 130, 130)


c.bind('<FocusIn>', in_focus)

root.mainloop()
'''
'''
from tkinter import *


def oval_func(event):
    c.delete(oval)
    c.create_text(80, 50,
                  text="Круг")


def rect_func(event):
    c.delete("rect")
    c.create_text(230, 50,
                  text="Прямоугольник")


def triangle(event):
    c.delete(trian)
    c.create_text(380, 50,
                  text="Треугольник")


c = Canvas(width=460, height=100,
           bg='grey80')
c.pack()

oval = c.create_oval(30, 10, 130, 80,
                     fill="orange")
c.create_rectangle(180, 10, 280, 80,
                   tag="rect",
                   fill="lightgreen")
trian = c.create_polygon(
    330, 80, 380, 10, 450, 80,# x,y koordinaten von 3 Ecken Dreieck
    fill='white', outline="black")

c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind("rect", '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)

mainloop()
'''
'''
from tkinter import *


def motion():
    #c.move(ball, 1, 0)
    c.move(ball, 0, 1)
    if c.coords(ball)[3] < 200:
        root.after(10, motion)


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
motion()
root.mainloop()
'''

from tkinter import *
root = Tk()
c = Canvas(width=300, height=300,
           bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140, 140, 160, 160,
                     fill='green')
c.bind('<Up>',
       lambda event: c.move(ball, 0, -12))# -12 hier piksel bei move in y coordinat
c.bind('<Down>',
       lambda event: c.move(ball, 0, 2))
c.bind('<Left>',
       lambda event: c.move(ball, -2, 0))
c.bind('<Right>',
       lambda event: c.move(ball, 2, 0))

root.mainloop()
