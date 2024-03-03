from threading import Thread
import os    
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import randint
import winsound


for _ in range(20):
    winsound.PlaySound("D:/GamesImade/pythonpong/bounce.wav", winsound.SND_FILENAME)


    for i in range(1):
        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        print(x)
        print(y)
        for _ in range(500000):
            brush = CreateSolidBrush(RGB(
                randint(0, 255),
                randint(0, 255),
                randint(0, 255)
                )) #Creates a brush
            SelectObject(desk, brush) #Choose that we're drawing with our brush.
            PatBlt(desk, randint(0, x), randint(0, y), randint(0, 100), randint(0, 200), PATCOPY)
            DeleteObject(brush)
            #Sleep(1) #wait
        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk) #Deletes our DC.
