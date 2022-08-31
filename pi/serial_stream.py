import time
import serial
import os
import logging
from tkinter import Tk, StringVar, Label

COMM_LENGTH = 4


def updateGUI(window: Tk, textInput: StringVar, message: str):
	logging.debug(f'updating GUI -> {message}')
	textInput.set(message)
	window.update()


def toggleAutoExposure(toggle: str):
	logging.debug(f'toggling auto exposure -> {toggle}')
	controls = {'0', '1'}
	if toggle in controls:
		os.system(f'/usr/bin/v4l2-ctl -c auto_exposure={toggle}')
	else:
		print(
			f'Error: Invalid command. Expected {", ".join(controls)} but got {toggle}.')


def parseCommand(window: Tk, textInput: StringVar, command: str):
    logging.debug(f'parsing command -> {command}')
    if len(command) < COMM_LENGTH:
        return
    comm_type = command[:COMM_LENGTH]
    comm_content = command[COMM_LENGTH + 1:]
    if comm_type == 'CHAT':
        updateGUI(window, textInput, comm_content),
    elif comm_type == 'EXPO':
        toggleAutoExposure(comm_content)


def readSerial(window: Tk, textInput: StringVar):
    try:
        ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
        output = ''
        logging.debug('Receiving serial responses from connected USB host...')
        while True:
            output = ser.readline().decode('utf-8')
            if len(output) > 0:
                parseCommand(window, textInput, output)
    except (FileNotFoundError, serial.SerialException):
        logging.error('Serial port not found.')


def main():
    logging.root.handlers = []
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(f'logs/{time.strftime("%Y-%m-%d")}.log'),
            logging.StreamHandler()])

    window = Tk()
    window.title('Project Pigeon')
    window.attributes('-fullscreen', True)
    window.configure(background='black')
    window.config(cursor='none')

    textInput = StringVar()
    label = Label(
        window,
        textvariable=textInput,
        font='Helvetica 64',
        wraplength=700,
        fg='#fff')
    label.place(relx=0, rely=.5, anchor='w')

    window.after(2000, readSerial, window, textInput)
    window.mainloop()


main()
