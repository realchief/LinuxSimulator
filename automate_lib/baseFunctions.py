#!/usr/bin/python

from __future__ import print_function

from keyboard import *
import pyautogui
import random
import time, csv, os
# import logging


# logging.basicConfig(level=logging.INFO, filename='auto-simulator.txt')

screenWidth, screenHeight = pyautogui.size()
print('Width: {}, Height: {}'.format(screenWidth, screenHeight))
stop_timea = 0.1
stop_timeb = 2


def get_pos():
    """
    get current position of mouse
    :return: (x, y)
    """
    return pyautogui.position()


def get_win_size():
    """
    get current size of window
    :return: screenWidth, screenHeight
    """
    return pyautogui.size()


def move_cursor(coor_x, coor_y):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """

    if coor_x == 0 and coor_y == 0:
        return
    action_time = random.uniform(0.1, 0.7)
    pyautogui.moveTo(coor_x, coor_y, action_time)


def move_click(coor_x, coor_y,  number=1):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """
    action_time = random.uniform(0.5, 1)
    pyautogui.moveTo(coor_x, coor_y, action_time)
    time.sleep(1)
    pyautogui.click(button='left', clicks=number)


def click_mouse(type, coor_x=None, coor_y=None):
    """
    Click mouse event with left, right.
    :param type: 
    :param coor_x: 
    :param coor_y: 
    :return: 
    """

    if coor_y == coor_x == None:
        time.sleep(random.uniform(stop_timea, stop_timeb))
        pyautogui.click(button=type)
    else:
        time.sleep(random.uniform(stop_timea, stop_timeb))
        pyautogui.click(x=coor_x, y=coor_y, button=type)


def scroll_mouse(count=1, sensivity=200, pause=0.5, sleep_time=.5):
    """
    if coor_x and coor_y is None, then scroll current position of cursor.
    :param amount_to_scroll: 
    :param coor_x: 
    :param coor_y: 
    :return: 
    """
    for i in range(0, count):
        try:
            # time.sleep(random.uniform(stop_timea, stop_timeb))
            print("scrolling: {} times".format(i))

            pyautogui.scroll(sensivity, pause=pause)
            time.sleep(sleep_time)
        except Exception as e:
            print("Scroll mouse Error: {}\n".format(e))


def random_move_cursor(num=10):
    """
    Random moving mouse cursor.
    :param num: 
    :return: 
    """
    count = 0
    while count < num:
        x = random.uniform(0, screenWidth)
        y = random.uniform(0, screenHeight)
        print(x, y)

        move_cursor(x, y)
        count += 1
        time.sleep(.5)


def type_of_object(obj):
    """
    Return type of object
    :param obj: 
    :return: 
    """

    obj_type = type(obj)
    print(obj_type.__name__)
    return obj_type.__name__


def classnames_unique(list):
    """
    Return classnames
    :param list: 
    :return: 
    """
    classnames = {v['class_name']: v for v in list}.values()
    print(classnames)
    return classnames


def start_menu():
    """
    Open start menu "application"
    :return: 
    """
    keyboard.hotkey('ALT', 'F1')


def search_app():
    """
    Run an application by typing
    :return: 
    """
    keyboard.hotkey('ALT', 'F2')


def parse_csv():
    urls = []
    try:
        with open(os.path.abspath('testurl.csv'), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                urls.append(row[1])
    except Exception as e:
        print('parse_csv Function => Got Error: {}'.format(e))

        with open('/home/ubuntu/workspace_ubuntu/automate_lib/testurl.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                urls.append(row[1])
    return urls

if __name__ == '__main__':
    move_cursor(coor_x=200, coor_y=500)