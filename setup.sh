#!/bin/bash

sudo apt-get install python3-pip -y
sudo pip3 install selenium
sudo pip3 install pynput
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz =o geckodriver.tar.gz -O geckodriver.tar.gz
tar xvzf geckodriver.tar.gz
rm geckodriver.tar.gz
sudo mv geckodriver /usr/bin
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
python3 driver.py
