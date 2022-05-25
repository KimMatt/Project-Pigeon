import time
import serial
from tkinter import Tk, StringVar, Label

def readSerial():
    while True:            
        try:
            ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
            output = ''
            print('Receiving serial responses from connected USB host...')
            while True:
                output = ser.readline().decode('utf-8')
                if len(output) > 0:
                    message.set(output)
                    window.update()
                time.sleep(1)
        except (FileNotFoundError, serial.SerialException):
            print('Serial port not found.')
            time.sleep(1)
            pass

window = Tk()
window.title('Project Pigeon')
window.attributes('-fullscreen', True)
window.configure(background='black')
window.config(cursor='none')

message = StringVar()
label = Label(window, textvariable=message, font='Helvetica 64', wraplength=700, fg='#fff')
label.place(relx=0, rely=.5, anchor='w')

window.after(2000, readSerial)
window.mainloop()

