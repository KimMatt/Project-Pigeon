# Project-Pigeon
Path to OBS

## Run Script on Pi Boot
Create a file with your favorite text editor at `/etc/xdg/autostart`:
```
sudo vim /etc/xdg/autostart/chat.desktop
```
Add the following contents to `chat.desktop`:
```
[Desktop Entry]
Name=Chat
Exec=/usr/bin/python3 /home/pi/Project-Pigeon/pi/serial_stream.py
```
On subsequent boots, your Raspberry Pi should run the chat GUI program on start.
