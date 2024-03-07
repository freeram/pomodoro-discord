import os
import sys
import json
from pygame import mixer

mixer.init()
beep = mixer.Sound('sounds/beep.mp3')

DEF_POMODORO_MINS = 25
DEF_SB_MINS = 5
DEF_LB_MINS = 10


def load_file(filename, on_no_file=None):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return on_no_file

    return data

def load_config():
    return load_file('config.json', {'theme': 'Default'})

def load_data():
    return load_file('data.json', None)

def save_config(config):
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

def reload_app():
    os.execl(sys.executable, sys.executable, *sys.argv)
