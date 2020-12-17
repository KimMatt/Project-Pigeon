import time
import serial
from tkinter import Tk, StringVar, Label

window = Tk()
window.title('Project Pigeon')
window.attributes('-fullscreen', True)

message = StringVar()
label = Label(window, textvariable=message, font='Helvetica 64')
label.place(relx=.5, rely=.5, anchor='center')

window.mainloop()

try:
    ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
    output = ''
    print('Receiving serial responses from connected USB host...')
    while True:
        output = ser.readline().decode('utf-8')
        if len(output) > 0:
            message.set(output)
        time.sleep(5)
except (FileNotFoundError, serial.SerialException):
    print('Serial port not found.')
