import vlc
import tkinter as tk
from tkinter import ttk

import sv_ttk

import pywinusb


window = tk.Tk()
window.title ("Robo Rover")
window.minsize (width=500, height=500)

sv_ttk.set_theme("dark")

button = ttk.Button(text="Click me!")
button.pack()

from pywinusb import hid

last = None

def handler(data):
    global last

    if last is None:
        last = data
        print(data)
        return

    for i, (old, new) in enumerate(zip(last, data)):
        if old != new:
            print(f"Byte {i}: {old} -> {new}")

    last = data.copy()

devices = hid.HidDeviceFilter().get_devices()

wheel = devices[28]
wheel.open()
wheel.set_raw_data_handler(handler)

input("Move wheel and pedals...")

def handler(data):
    steering = data[1] | (data[2] << 8)
    print(steering)
wheel.close()


# player = vlc.MediaPlayer('test.mp4')
# player.play()
# player.get_instance()