import time
import serial
import os
from tkinter import Tk, StringVar, Label

COMM_LENGTH = 4

def updateGUI(window: Tk, textInput: StringVar, message: str):
	textInput.set(message)
	window.update()

def toggleAutoExposure(toggle: str):
	controls = { '0', '1' }
	if toggle in controls:
		os.system(f'/usr/bin/v4l2-ctl -c auto_exposure={toggle}')
	else:
		print(f'Error: Invalid command. Expected {", ".join(controls)} but got {toggle}.')

def parseCommand(window: Tk, textInput: StringVar, command: str):
	if len(command) < COMM_LENGTH:
		return
	comm = command[:COMM_LENGTH -1]
	return {
		'CHAT': updateGUI(window, textInput, command[COMM_LENGTH + 1:]),
		'EXPO': toggleAutoExposure(command[COMM_LENGTH + 1:])
	}[comm]

def readSerial(window: Tk, textInput: StringVar):
    while True:            
        try:
            ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
            output = ''
            print('Receiving serial responses from connected USB host...')
            while True:
                output = ser.readline().decode('utf-8')
                if len(output) > 0:
                    parseCommand(window, textInput, output)

        except (FileNotFoundError, serial.SerialException):
            print('Serial port not found.')
            time.sleep(1)
            pass

window = Tk()
window.title('Project Pigeon')
window.attributes('-fullscreen', True)
window.configure(background='black')
window.config(cursor='none')

textInput = StringVar()
label = Label(window, textvariable=textInput, font='Helvetica 64', wraplength=700, fg='#fff')
label.place(relx=0, rely=.5, anchor='w')

window.after(2000, readSerial)
window.mainloop()

