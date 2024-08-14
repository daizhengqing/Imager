import json
import os

def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

def write_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)

if (os.path.exists('config.json') == False):
    write_config({
      "dirs": []
    })