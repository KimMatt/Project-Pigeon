import usb.core
import usb.util
import sys
import numpy as np

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

print(device.bLength)
print(device.bNumConfigurations)
print(device.bDeviceClass)

cfg = device[0]
intf = cfg[(0,0)]
ep = intf[0]
assert ep is not None

while True:
    if np.random.rand() > 0.5:
        ep.write('0',1000)
    else:
        ep.write('1',1000)


