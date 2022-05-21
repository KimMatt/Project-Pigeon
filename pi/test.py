import time
import serial

def readSerial():
    try:
        ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
        output = ''
        print('Receiving serial responses from connected USB host...')
        while True:
            output = ser.readline().decode('utf-8')
            if len(output) > 0:
                print(output)
            time.sleep(1)
    except (FileNotFoundError, serial.SerialException):
        print('Serial port not found.')

readSerial()
