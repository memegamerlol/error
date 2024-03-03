from threading import Thread
import os    
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import randint
import ctypes
import numpy as np
import sounddevice as sd
import messagebox
import time
from threading import Thread
from random import *
import winsound
import ctypes
import numpy as np
import sounddevice as sd

messagebox.askyesno("error make by memegamerlol", "this is GDI-malware run?")


messagebox.askyesno("error made by memegamerlol","are you sure?")


messagebox.askyesno("warning EPILEPTIC","THIS MALWARE HAS FLASHING LIGHTS NOT FOR EPILEPTIC")


def bytebeat(t):
   
    return ((t>>12|t>>8)&63&t>>4) & 0xFF


duration = 60  
sample_rate = 44100  


t_values = np.arange(0, duration * sample_rate)
audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8)


sd.play(audio_data, sample_rate)






# Define colors
red = 'red'
green = 'green'
purple = 'purple'


def flash_screen(color):
    hdc = GetDC(0)  # Get the screen as a Device Context object
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)  # Retrieve monitor size
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert the device context
    time.sleep(0.1)  # Sleep for 100 milliseconds
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert back to normal
    DeleteDC(hdc)  # Clean up memory


def check_vpn_status():
    # Replace this function with your actual VPN status check logic
    # For demonstration purposes, we'll assume VPN is down half the time
    return time.time() % 2 == 0


if __name__ == "__main__":
    for _ in range(21):
        if check_vpn_status():
            flash_screen(green)  # VPN is up (steady green)
        else:
            flash_screen(red)  # VPN is down (blinking red)


import sys
import ctypes
import time
from win32con import PATINVERT
from win32gui import GetDC, PatBlt
import tkinter as tk
import tkinter as tk
from random import choice, randint
from string import ascii_letters

# Constants for screen dimensions
SM_CXSCREEN = 0
SM_CYSCREEN = 1

def get_screen_dimensions():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(SM_CXSCREEN)
    screen_height = user32.GetSystemMetrics(SM_CYSCREEN)
    return screen_width, screen_height

def screen_melter(dc, duration=1000):
    screen_width, screen_height = get_screen_dimensions()
    x, y = 0, 0
    w, h = screen_width, screen_height

    start_time = time.time()
    while time.time() - start_time < duration:
        PatBlt(dc, x, y, w, h, PATINVERT)
        time.sleep(0.01)

def main():
    dc = GetDC(0)
    screen_melter(dc, duration=10)

if __name__ == "__main__":
    print(f"Python {' '.join(elem.strip() for elem in sys.version.split('\\n'))} {'64' if sys.maxsize > 0x100000000 else '32'}bit on {sys.platform}")
    main()
    print("\nDone.")

for i in range(1):
        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        print(x)
        print(y)
        #os.startfile('guiCorrupt.py')
        for i in range(1000):
            brush = CreateSolidBrush(RGB(
                randrange(25550),
                randrange(25550),
                randrange(25550)
                )) #Creates a brush
            SelectObject(desk, brush) #Choose that we're drawing with our brush.
            PatBlt(desk, randrange(x), randrange(y), randrange(100), randrange(200), PATCOPY)
            DeleteObject(brush)
            #Sleep(1) #wait
        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk) #Deletes our DC.


        # Constants for screen dimensions
SM_CXSCREEN = 0
SM_CYSCREEN = 1

def get_screen_dimensions():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(SM_CXSCREEN)
    screen_height = user32.GetSystemMetrics(SM_CYSCREEN)
    return screen_width, screen_height

def screen_melter(dc, duration=10):
    screen_width, screen_height = get_screen_dimensions()
    x, y = 0, 0
    w, h = screen_width, screen_height

    start_time = time.time()
    while time.time() - start_time < duration:
        PatBlt(dc, x, y, w, h, PATINVERT)
        time.sleep(0.01)

def main():
    dc = GetDC(0)
    screen_melter(dc, duration=10)

if __name__ == "__main__":
    print(f"Python {' '.join(elem.strip() for elem in sys.version.split('\\n'))} {'64' if sys.maxsize > 0x100000000 else '32'}bit on {sys.platform}")
    main()
    print("\nDone.")



    for i in range(1):
        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        print(x)
        print(y)
        #os.startfile('guiCorrupt.py')
        for i in range(1000):
            brush = CreateSolidBrush(RGB(
                randrange(25550),
                randrange(25550),
                randrange(25550)
                )) #Creates a brush
            SelectObject(desk, brush) #Choose that we're drawing with our brush.
            PatBlt(desk, randrange(x), randrange(y), randrange(100), randrange(200), PATCOPY)
            DeleteObject(brush)
            #Sleep(1) #wait
        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk) #Deletes our DC.




def bytebeat(t):
   
    return ((t>>12|t>>8)&63&t>>40) & 0xFF


duration = 60  
sample_rate = 44100  


t_values = np.arange(0, duration * sample_rate)
audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8)


sd.play(audio_data, sample_rate)


# Define colors
red = 'red'
green = 'green'
purple = 'purple'


def flash_screen(color):
    hdc = GetDC(0)  # Get the screen as a Device Context object
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)  # Retrieve monitor size
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert the device context
    time.sleep(0.1)  # Sleep for 100 milliseconds
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert back to normal
    DeleteDC(hdc)  # Clean up memory


def check_vpn_status():
    # Replace this function with your actual VPN status check logic
    # For demonstration purposes, we'll assume VPN is down half the time
    return time.time() % 2 == 0


if __name__ == "__main__":
    for _ in range(21):
        if check_vpn_status():
            flash_screen(green)  # VPN is up (steady green)
        else:
            flash_screen(red)  # VPN is down (blinking red)



            def screen_effect_tunnel():
                dc = GetDC(0)
                screen_width, screen_height = get_screen_dimensions()
                x, y = 0, 0
                w, h = screen_width, screen_height

                start_time = time.time()
                while time.time() - start_time < 10:
                    PatBlt(dc, x, y, w, h, PATINVERT)
                    x += 10
                    y += 10
                    w -= 20
                    h -= 20
                    time.sleep(0.01)

            if __name__ == "__main__":
                screen_effect_tunnel()

                def memz_gdi_effect():
                    dc = GetDC(0)
                    screen_width, screen_height = get_screen_dimensions()
                    x, y = 0, 0
                    w, h = screen_width, screen_height

                    start_time = time.time()
                    while time.time() - start_time < 10:
                        PatBlt(dc, x, y, w, h, PATINVERT)
                        x += 10
                        y += 10
                        w -= 20
                        h -= 20
                        time.sleep(0.01)

                if __name__ == "__main__":
                    memz_gdi_effect()
                    
                    def random_lines_effect():
                        dc = GetDC(0)
                        screen_width, screen_height = get_screen_dimensions()

                        start_time = time.time()
                        while time.time() - start_time < 10:
                            x1 = randint(0, screen_width)
                            y1 = randint(0, screen_height)
                            x2 = randint(0, screen_width)
                            y2 = randint(0, screen_height)
                            PatBlt(dc, x1, y1, x2, y2, PATINVERT)
                            time.sleep(0.01)

                    if __name__ == "__main__":
                        random_lines_effect()


                        def random_shapes_effect():
                            dc = GetDC(0)
                            screen_width, screen_height = get_screen_dimensions()

                            start_time = time.time()
                            while time.time() - start_time < 10:
                                shape = randint(0, 2)  # Randomly choose a shape (0: rectangle, 1: ellipse, 2: round rectangle)
                                x = randint(0, screen_width)
                                y = randint(0, screen_height)
                                width = randint(10, 200)
                                height = randint(10, 200)
                                PatBlt(dc, x, y, width, height, shape)
                                time.sleep(0.01)

                                def screen_spin_effect():
                                    dc = GetDC(0)
                                    screen_width, screen_height = get_screen_dimensions()
                                    x, y = 0, 0
                                    w, h = screen_width, screen_height

                                    start_time = time.time()
                                    while time.time() - start_time < 10:
                                        PatBlt(dc, x, y, w, h, PATINVERT)
                                        x += 10
                                        y += 10
                                        w -= 20
                                        h -= 20
                                        time.sleep(0.01)

                                if __name__ == "__main__":
                                    screen_spin_effect()
                                    def screen_destruction_effect():
                                        dc = GetDC(0)
                                        screen_width, screen_height = get_screen_dimensions()

                                        start_time = time.time()
                                        while time.time() - start_time < 10:
                                            x = randint(0, screen_width)
                                            y = randint(0, screen_height)
                                            width = randint(10, 200)
                                            height = randint(10, 200)
                                            PatBlt(dc, x, y, width, height, PATINVERT)
                                            time.sleep(0.01)

                                    if __name__ == "__main__":
                                        screen_destruction_effect()

                                        def screen_melter_with_textboxes():
                                            root = tk.Tk()
                                            root.title("Screen Melter with Textboxes")
                                            
                                            screen_width, screen_height = get_screen_dimensions()
                                            x, y = 0, 0
                                            w, h = screen_width, screen_height
                                            
                                            canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='black')
                                            canvas.pack()
                                            
                                            textboxes = []
                                            
                                            def create_textbox():
                                                x = randint(0, screen_width)
                                                y = randint(0, screen_height)
                                                text = ''.join(choice(ascii_letters) for _ in range(10))
                                                textbox = canvas.create_text(x, y, text=text, fill='white')
                                                textboxes.append(textbox)
                                            
                                            def move_textboxes():
                                                for textbox in textboxes:
                                                    dx = randint(-10, 10)
                                                    dy = randint(-10, 10)
                                                    canvas.move(textbox, dx, dy)
                                            
                                            def screen_melter_loop():
                                                PatBlt(dc, x, y, w, h, PATINVERT)
                                                move_textboxes()
                                                root.after(10, screen_melter_loop)
                                            
                                            root.after(0, create_textbox)
                                            root.after(10, screen_melter_loop)
                                            root.mainloop()

                                        if __name__ == "__main__":
                                            def screen_melter_with_textboxes():
                                                root = tk.Tk()
                                                root.title("Screen Melter with Textboxes")
                                                
                                                screen_width, screen_height = get_screen_dimensions()
                                                x, y = 0, 0
                                                w, h = screen_width, screen_height
                                                
                                                canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='black')
                                                canvas.pack()
                                                
                                                textboxes = []
                                                
                                                def create_textbox():
                                                    x = randint(0, screen_width)
                                                    y = randint(0, screen_height)
                                                    text = ''.join(choice(ascii_letters) for _ in range(10))
                                                    textbox = canvas.create_text(x, y, text=text, fill='white')
                                                    textboxes.append(textbox)
                                                
                                                def move_textboxes():
                                                    for textbox in textboxes:
                                                        dx = randint(-10, 10)
                                                        dy = randint(-10, 10)
                                                        canvas.move(textbox, dx, dy)
                                                
                                                def screen_melter_loop():
                                                    PatBlt(dc, x, y, w, h, PATINVERT)
                                                    move_textboxes()
                                                    root.after(10, screen_melter_loop)
                                                
                                                root.after(0, create_textbox)
                                                root.after(10, screen_melter_loop)
                                                root.mainloop()

                                            screen_melter_with_textboxes()
                                        def screen_trasher():
                                            dc = GetDC(0)
                                            screen_width, screen_height = get_screen_dimensions()

                                            start_time = time.time()
                                            while time.time() - start_time < 10:
                                                x = randint(0, screen_width)
                                                y = randint(0, screen_height)
                                                width = randint(10, 200)
                                                height = randint(10, 200)
                                                PatBlt(dc, x, y, width, height, PATINVERT)
                                                time.sleep(0.01)

                                        if __name__ == "__main__":
                                            screen_trasher()

                                            def bytebeat_music():
                                                # Your bytebeat music code goes hereef bytebeat(t):
                                                pass

                                            if __name__ == "__main__":
                                                duration = 60  
                                                bytebeat_music()
                                                sample_rate = 44100  

                                                t_values = np.arange(0, duration * sample_rate)
                                                audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8)

                                                sd.play(audio_data, sample_rate)

                                            bytebeat_music()

                                            def screen_slider_effect():
                                                dc = GetDC(0)
                                                screen_width, screen_height = get_screen_dimensions()
                                                x, y = 0, 0
                                                w, h = screen_width, screen_height

                                                start_time = time.time()
                                                while time.time() - start_time < 10:
                                                    PatBlt(dc, x, y, w, h, PATINVERT)
                                                    x += 10
                                                    time.sleep(0.01)

                                            if __name__ == "__main__":
                                                if __name__ == "__main__":
                                                    if __name__ == "__main__":
                                                        screen_slider_effect()
