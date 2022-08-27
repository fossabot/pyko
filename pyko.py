## Pyko Framework
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
from hacking.hackerman import *
from hacking.zombies import *
from dev.colors import *
from dev.mm import *
import platform

# Attributes
hackerman = Hackerman()
def detect():
    os_detect = platform.system()
    return os_detect
def clear():
    if detect() == '':
        sh("rmdir /s __pycache__ && rmdir /s hacking\__pycache__ && rmdir /s dev\__pycache__")
    elif 'win' in detect():
        sh("rmdir /s __pycache__ && rmdir /s hacking\__pycache__ && rmdir /s dev\__pycache__")
        # elif 'bsd' in os_dectect: -> Add your system here
    else: # Linux
        sh("rm -rf __pycache__ && rm -rf hacking/__pycache__ && rm -rf dev/__pycache__")
