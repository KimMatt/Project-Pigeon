import time
import serial

COMM_LENGTH = 4

def parseCommand(command: str):
    if len(command) < COMM_LENGTH:
        return
    comm_type = command[:COMM_LENGTH]
    comm_content = command[COMM_LENGTH + 1:]
    if comm_type == 'CHAT':
        print('CHAT: ' + comm_content)
    elif type == 'EXPO':
        print('AUTO EXPOSURE: ' + comm_content)

def readSerial():
    try:
        ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
        output = ''
        print('Receiving serial responses from connected USB host...')
        while True:
            output = ser.readline().decode('utf-8')
            if len(output) > 0:
                parseCommand(output)
            time.sleep(1)
    except (FileNotFoundError, serial.SerialException):
        print('Serial port not found.')

readSerial()
