import tkinter
import time
import threading

root = tkinter.Tk()

height1 = 500
width1 = 500

myCanvas = tkinter.Canvas(root, bg='white', height = height1, width = width1)

def drawRect(posx, posy):
    coords = 10,10,posx,posy
    rect = myCanvas.create_rectangle(coords, fill='black')

def runCan():
    myCanvas.pack()
    root.mainloop()

drawRect(100,100)
runCan()

drawRect(300,300)
runCan()

