import time
import serial
import os
import logging
from tkinter import Tk, StringVar, Label


COMM_LENGTH = 4
LOG_FILE = f'Project-Pigeon/pi/logs/{time.strftime("%Y-%m-%d")}.log'


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


def setExposure(time: str):
    logging.debug(f'setting absolute exposure -> {time}')
    os.system(f'/usr/bin/v4l2-ctl -c exposure_time_absolute={time}')


def parseCommand(window: Tk, textInput: StringVar, command: str):
	logging.debug(f'parsing command -> {command[:-1]}')
    if len(command) < COMM_LENGTH:
        return
    comm_type = command[:COMM_LENGTH]
    comm_content = command[COMM_LENGTH + 1:-1]
    if comm_type == 'CHAT':
        updateGUI(window, textInput, comm_content),
    elif comm_type == 'EXPO':
        toggleAutoExposure(comm_content)
    elif comm_type == 'EXTM':
        setExposure(comm_content)


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
        window.destroy()
        os.system(f'nano {LOG_FILE}')


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, mode='a', encoding=None, delay=False),
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
