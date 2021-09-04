from os.path import expanduser
from pathlib import Path
import os
from LOGGER import *

home = str(Path.home())
FULL_USER_DIRECTORIES = home + "\\.config\\PrintLion"

def CONFIG_FILE_CREATE():
    PLUGIN_DIR = os.path.join(FULL_USER_DIRECTORIES,"plugins.json")
    PRESETS_DIR = os.path.join(FULL_USER_DIRECTORIES,"presets.json")
    if not os.path.exists(PLUGIN_DIR):
        PLUGIN_FILE = open(PLUGIN_DIR, "w")
    else:
        LOGS.PLUGIN_DIR_EXISTS()
    if not os.path.exists(PRESETS_DIR):
        PRESETS_FILE = open(PRESETS_DIR, "w")
    else:
        LOGS.PRESETS_DIR_EXISTS()
        
if not os.path.exists(FULL_USER_DIRECTORIES):
    os.mkdir(FULL_USER_DIRECTORIES)
    CONFIG_FILE_CREATE()
else:
    LOGS.DIRECTORY_EXISTS()
    CONFIG_FILE_CREATE()
