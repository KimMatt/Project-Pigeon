import usb.core
import usb.util
import sys

device = usb.core.find(idVendor=0x1d6b, idProduct=0x0002)

if device is None:
    sys.exit('Could not find device. Check idVendor and idProduct matches lsusb -v info')

if device.is_kernel_driver_active(0):
    try:
        device.detach_kernel_driver(0)
        print('kernel driver detatched')
    except usb.core.USBError as e:
        print('could not detatch kernel driver:{}'.format(str(e)))

device.set_configuration()

ep = device[0][(0,0)][0]

assert ep is not None

while True:
    try:
        data = ep.read(ep.wMaxPacketSize, 10000)
        print(data)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
