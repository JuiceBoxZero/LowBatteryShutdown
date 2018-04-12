# LowBatteryShutdown
This script, when run with a connected JuiceBox Zero will trigger an automatic shutdown sequence when the attached Li-Ion battery reaches 3.2v.

## Usage
To install this software without having to manually create the file and copy/paste the code, do the following:
This is assuming you have set up your Raspberry Pi with a monitor, internet connection(Ethernet or WIFI), keyboard and mouse connected directly. 

Open a terminal and type the following to make sure your Pi is updated (This could take a few minutes):
```
sudo apt-get update
sudo apt-get upgrade
```
Then type the following to actually download the code:
```
git clone https://github.com/JuiceBoxZero/LowBatteryShutdown.git
```
Now you need to run the setup, so get into the newly downloaded folder by typing:
```
cd LowBatteryShutdown
```
and run the setup by typing:
```
sudo python setup.py install
```
Then, to make sure the code runs in the background, you'll create a crontab.
Do this by typing:
```
sudo crontab -e
```
(select a text editor, usually "Nano" is the default option)
At the bottom of the file add the line:
```
@reboot sudo python /home/pi/LowBatteryShutdown/LowBatteryShutdown.py &
```
Now save and exit.
Then, reboot your Pi with:
```
sudo reboot -n
```
That's it!
Your Pi will automatically shut down (safely!) whenever JuiceBox Zero is connected to your Pi and the Low Battery indicator goes to a logic HIGH.

*****
It is important to note that you must completely disconnect power to the Pi before it can be turned back on again. 
Do this by simply sliding the power switch to the off position and then back on again. Your Pi will power up like normal.
*****

In case you need to change anything, the python script that is running in the background is located here:
```
/home/pi/LowBatteryShutdown/
```
and is called:
```
LowBatteryShutdown.py
```

Type ```sudo nano /home/pi/LowBatteryShutdown/LowBatteryShutdown.py``` to look at and/or edit the file. 
