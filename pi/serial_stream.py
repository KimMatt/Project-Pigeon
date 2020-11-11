import serial

ser = serial.Serial('/dev/ttyGS0', 115200, 8, 'N', 1, timeout=1)
output = ""

print("Receiving serial responses from connected USB host...")
while True:
    output = ser.readline()
    if len(output) > 0:
        print(output)