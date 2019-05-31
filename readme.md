# OpenWay - Test task
## author: Anastasia Ivanova

## Install dependencies
`pip3 install -r requirements.txt` - install all python dependencies

Actually, you should load a chrome webdriver into this directory. 
For example here placed a webdriver for windows OS.

## Run script
`python3 main.py`

## Login and password
Into source code you can find `login` and `passwd` variables. You can change their values for your login and password and start a script. 

## Some Notes
I found some interesting issues when i test my script. For example sometimes yandex change their page design and script setting become not relevant and script restarting.

Moreover I seem what sometimes yandex show some strange windows what crash my script, so it also tries to restart.