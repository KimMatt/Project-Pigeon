import time
import serial
from tkinter import *

window = Tk()
window.title("Project Pigeon")
window.attributes("-fullscreen", True)

message = Label(window, text="elonmusk: EZ Clap", font="Helvetica 48")
message.place(relx=.5, rely=.5, anchor="center")

window.mainloop()

try:
    ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
    output = ""
    print("Receiving serial responses from connected USB host...")
    while True:
        output = ser.readline()
        if len(output) > 0:
            print(output)
        time.sleep(1)
except (FileNotFoundError, serial.serialutil.SerialException):
    print("Serial port not found.")
