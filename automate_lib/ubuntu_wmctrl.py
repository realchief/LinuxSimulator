import subprocess
from time import sleep
import re
import sys
import shlex
import argparse

# Make sure xdotools is installed
try:
    subprocess.Popen('wmctrl', stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
except OSError as e:
    if 'No such file' in e.args[1]:
        print("ERROR: The program 'wmctrl' is not installed. Use " \
              "'sudo apt-get install wmctrl' to install it.")
        sys.exit(1)

PRODUCE_SCRIPT = False
LAUNCHED = []