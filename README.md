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
```
