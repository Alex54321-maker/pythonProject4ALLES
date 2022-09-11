from tkinter import *

game_width = 500
game_height = 500
snake_item = 10
snake_color1 = "red"
snake_color2 = "yellow"
snake_x = 24
snake_y = 24

tk = Tk()
tk.title("Spiel Schlange auf Py")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = game_width,height = game_height,bd =0, highlightthickness = 0)
canvas.pack()
tk.update()

def snake_paint_item(canvas, x, y):
    canvas.create_rectangle(x*snake_item,y*snake_item, x*snake_item+snake_item,y*snake_item+snake_item,fill=snake_color2)
    canvas.create_rectangle(x*snake_item+2,y*snake_item+2, x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=snake_color1)
    #если +2 то координаты смещаются от первых также и отымаются - 2 получается квадрат в квадрате
snake_paint_item(canvas, snake_x, snake_y)

tk.mainloop()
