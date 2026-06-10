import vlc
import tkinter as tk
from tkinter import ttk

import sv_ttk
from PIL import Image, ImageTk

import pywinusb
from pywinusb import hid

import serial
from serial_comms import *
import time


s = serial.Serial('COM8', 9600)  
time.sleep(2)  

last = None


def send_inputs(byte1, byte2, byte9, byte10):

    s.write(bytes([
        byte1, 
        byte2, 
        byte9, 
        byte10
    ]))



def reader(data):
    

    # get left/right  
    
    a = data[1]
    b = data[2]
    
   


    steering = a | b << 8

    if steering > 32768:
        left_percent = (32768 - steering) / 32768 * 100
        # print(left_percent)
    if steering < 32768:
        right_percent = (steering - 32768) / 32768 * 100
        # print(right_percent) 
        

        # print(result)

        # get forward/backwards acceleration (128 - 32768 - 65408)

    c = data[9]
    d = data[10]
    
     #send steering bits and pedals to arduino
    send_inputs(a, b, c, d)
    # acceleration(c, d)

    accel = c | d << 8

    result = accel

    # print(result)

    
    

devices = hid.HidDeviceFilter().get_devices()

wheel = devices[28]
wheel.open()
wheel.set_raw_data_handler(reader)

input("Move wheel and pedals...")


