# LowBatteryShutdown
This script, when run with a connected JuiceBox Zero will trigger an automatic shutdown sequence when the attached Li-Ion battery reaches 3.2v.

## Usage
To install this software without having to manually create the file and copy/paste the code, do the following:
```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/JuiceBoxZero/LowBatteryShutdown.git
cd LowBatteryShutdown
sudo python setup.py install
sudo crontab -e
(select a text editor, usually "Nano" is the default option)
At the bottom of the editor add the line:
@reboot sudo python /home/pi/JuiceBoxZero/LowBatteryShutdown.py
Save and exit
```
Reboot your Pi with

```
sudo reboot -n
```

Your Pi will automatically shut down (safely!) whenever JuiceBox Zero is connected to your Pi and the Low Battery indicator goes to a logic HIGH.
