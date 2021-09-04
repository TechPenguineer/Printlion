from os.path import expanduser
from pathlib import Path
import os
from LOGGER import *

home = str(Path.home())
FULL_USER_DIRECTORIES = home + "\\.config\\Printlion"

def CONFIG_FILE_CREATE():
    if not os.path.exists(FULL_USER_DIRECTORIES + "\\plugins.json"):
        os.write(FULL_USER_DIRECTORIES+"\\plugins.json")
    else:
        LOGS.PLUGIN_DIR_EXISTS()
if not os.path.exists(FULL_USER_DIRECTORIES):
    os.mkdir(FULL_USER_DIRECTORIES)
else:
    LOGS.DIRECTORY_EXISTS()
