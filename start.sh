#!/bin/sh
cd /home/pi/Desktop/ContadorRasp
sudo pigpiod &
sudo python3 main.py &
sudo php /home/pi/Desktop/checkConnectionStatus.php &
