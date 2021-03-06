import subprocess
from time import sleep
import re
import sys
import shlex
import argparse

# Make sure xdotools is installed
try:
    subprocess.Popen('xdotool', stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
except OSError as e:
    if 'No such file' in e.args[1]:
        print("ERROR: The program 'xdotool' is not installed. Use " \
              "'sudo apt-get install xdotool' to install it.")
        sys.exit(1)

PRODUCE_SCRIPT = False
LAUNCHED = []


# ------------------------- Starting processes -------------------------

def pid_to_cmd(pid):
    ''' Get the command to a process'''
    out = get_cmd_output('ps -o args %s' % pid)
    return out[0].split('\n')[1].strip()


def run_cmd(cmd):
    ''' Run a command '''
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return proc


def get_proc_output(proc):
    out, err = proc.communicate()
    return out.decode("UTF-8"), err.decode("UTF-8")


def get_cmd_output(cmd):
    ''' Run a command and get its output'''
    return get_proc_output(run_cmd(cmd))


def launch(cmd):
    ''' Run a gui application '''
    open_windows = current_windows()
    proc = run_cmd(cmd)

    # Wait for new proc to open GUI
    while (open_windows == current_windows()):
        sleep(0.2)

    new_wids = [wid for wid in current_windows() if wid not in open_windows]
    if len(new_wids) > 1:
        print('ERROR: launch(): too many window ids found')
        return None
    if len(new_wids) < 1:
        print('ERROR: launch(): too few window ids found')
        return None
    LAUNCHED.append([cmd, wid])
    wid = int(new_wids[0], 16)
    pid = win_pid(wid)
    return wid, pid


# -------------------------------- X Win -------------------------------

def xdo(do):
    out, err = get_cmd_output('xdotool ' + do)
    if err:
        print('ERROR: %s' % err)
    return out


def win_pid(wid):
    ''' Gives the PID of the process that window belongs to '''
    return xdo('getwindowpid %s' % wid).strip()


def search_pid():
    ''' Search activation pid of window'''
    return xdo('search --onlyvisible --')


def current_windows():
    ''' Gives a list with all open windows '''
    out, err = get_cmd_output('xprop -root')
    match = re.search(r'_NET_CLIENT_LIST_STACKING\(WINDOW\): window id # (.*)', out)
    if not match:
        return None
    return match.group(1).split(', ')


def win_name(wid):
    ''' Gives the name of a window '''
    return xdo('getwindowname %s' % wid).strip()


def win_size(wid, x=None, y=None):
    if x is None or y is None:
        out = xdo('getwindowgeometry %s' % wid)
        match = re.search(r'Geometry: (.*)', out)
        if not match:
            return None
        return map(int, match.group(1).split('x'))
    else:
        xdo('windowsize %s %s %s' % (wid, x, y))


def win_pos(wid, x=None, y=None):
    if x is None or y is None:
        out = xdo('getwindowgeometry %s' % wid)
        match = re.search(r'Position: (\d*,\d*)', out)
        if not match:
            return None
        return map(int, match.group(1).split(','))
    else:
        xdo('windowmove %s %s %s' % (wid, x, y))


def win_screen(wid):
    out = xdo('getwindowgeometry %s' % wid)
    match = re.search(r'Position: \d*,\d* \(screen: (\d*)\)', out)
    if not match:
        return None
    return int(match.group(1))


def win_desktop(wid, desktop=None):
    ''' Gives the desktop number of the given window '''
    if desktop is None:
        return int(xdo('get_desktop_for_window %s' % wid).strip())
    else:
        return xdo('set_desktop_for_window %s %desktop' % (wid, desktop))


def win_exists(wid):
    out, err = get_cmd_output('xdotool getwindowname %s' % wid)
    if err:
        return False
    else:
        return True


# ---------------------- Auto generating scripts -----------------------

class scriptify:
    script_header = """#! /usr/bin/python\n""" \
                    """# script generated by winlaunch\n""" \
                    """from winlaunch import *\n\n"""

    @staticmethod
    def launched_windows(filename='launch_script.py'):
        f = open(filename, 'w')

        lines = []
        for cmd, wid in LAUNCHED:
            if win_exists(wid):
                name = win_name(wid).split(' - ')[-1]
                lines.append("# %s" % name)
                lines.append("wid, pid = launch('%s')" % cmd)
                lines.append("win_size(wid, %s, %s)" % tuple(win_size(wid)))
                lines.append("win_pos(wid, %s, %s)" % tuple(win_pos(wid)))
                lines.append("win_desktop(wid, %s)" % win_desktop(wid))
                lines.append("")

        f.write(scriptify.script_header)
        for line in lines:
            f.write(line + '\n')
        f.close()

        return filename

    @staticmethod
    def open_windows(filename='launch_script.py'):
        f = open(filename, 'w')

        lines = []
        for wid in current_windows():
            if win_exists(wid):
                pid = win_pid(wid)
                name = win_name(wid).split(' - ')[-1]
                lines.append("# %s" % name)
                lines.append("wid, pid = launch('%s')" % pid_to_cmd(pid))
                lines.append("win_size(wid, %s, %s)" % tuple(win_size(wid)))
                lines.append("win_pos(wid, %s, %s)" % tuple(win_pos(wid)))
                lines.append("win_desktop(wid, %s)" % win_desktop(wid))
                lines.append("")

        f.write(scriptify.script_header)
        for line in lines:
            f.write(line + '\n')
        f.close()

        return filename


# ---------------------- Running as program -----------------------


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("generate-script", help="Takes a snapshot of currently open windows and " + \
                                                "creates a Python script that can be used to launch" + \
                                                "windows again.")
    args = parser.parse_args()
    if "generate-script" in args:
        filename = scriptify.open_windows()
        print("Generated script as %s" % filename)


if __name__ == '__main__':
    main()
