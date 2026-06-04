import vlc
import tkinter as tk
from tkinter import ttk

import sv_ttk
from PIL import Image, ImageTk

import pywinusb
from pywinusb import hid


window = tk.Tk()
window.title("Robo Rover")
window.minsize(width=500, height=500)

# Background image
bg_image = Image.open("wheel.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


last = None

def reader(data):
    

    # get left/right  
    
    a = data[1]
    b = data[2]
    
    steering = a | b << 8

    if steering > 32768:
        left_percent = (32768 - steering) / 32768 * 100
        print(left_percent)
    if steering < 32768:
        right_percent = (steering - 32768) / 32768 * 100
        print(right_percent) 
        

    # print(result)

    # get forward/backwards acceleration (128 - 32768 - 65408)
    # a = data[9]
    # b = data[10]
    
    # accel = a | b << 8

    # result = accel

    # print(result)

    
    

devices = hid.HidDeviceFilter().get_devices()

wheel = devices[28]
wheel.open()
wheel.set_raw_data_handler(reader)

input("Move wheel and pedals...")


# def convert(data)

# player = vlc.MediaPlayer('test.mp4')
# player.play()
# player.get_instance()