#!/usr/bin/python


from __future__ import print_function
from baseFunctions import *
import subprocess
import sys
import pyautogui
import random
import time
from const import *
import logging

stop_intervala = 0.007
stop_intervalb = 0.2
pyautogui.FAILSAFE = False

keys = {
    'digits': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'operators': ['*', '+', ',', '-', '.', '/', '^'],
    'comparisons': ['<', '=', '>'],
    'specials': ['!', '"', '#', '$', '%', '&', "'", ':', ';', '?', '@', '_', '\\', '`',
                 '~', '|'],
    'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'backspace': [' ', '\t', '\n', '\r'],
    'brackets': ['(', ')', '{', '}', '[', ']'],
    'modifier': ['alt', 'altleft', 'altright', 'capslock', 'clear', 'shift', 'shiftleft', 'shiftright',
                 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'enter', 'esc', 'escape', 'execute', 'backspace'],
    'fn': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']
}


class Keyboard():
    def __init__(self):
        print('Starting to control the keyboard')

    def typewrite(self, txt):
        """
        Write something text.
        :param txt: 
        :param interval: 
        :return: 
        """
        print('content: {}'.format(txt))

        words_list = str(txt).replace('\n\n', '\n').split(' ')

        line_count = 1
        scroll_flag = False
        paragraph_line = random.choice([3, 4, 5])
        print('paragraph_line: {}'.format(paragraph_line))

        for word in words_list:
            try:
                back_count = 0
                # if line_count
                if '\n' in word:
                    print('word: {}'.format(word))
                    line_count += 1
                    print('exist n: {}'.format(line_count))
                    scroll_flag = True

                # if reaches to 11 lines, then scroll up and down twice.
                if scroll_flag and line_count % paragraph_line == 0:
                    print('next line')
                    scroll_flag = False

                else:
                    print('remove {}'.format(line_count))
                    word.replace("\n|\r\n", " ")

                interval = random.uniform(stop_intervala, stop_intervalb)
                pyautogui.typewrite(word, interval=interval)

                if all(char.isalpha() for char in word):  # if includes special character, pass it.
                    back_count = self.get_backspace_count(len(word))

                if back_count != 0:  # Backspace
                    for i in range(back_count):
                        self.hotkey('backspace')
                    time.sleep(1)
                    pyautogui.typewrite(word[-back_count:], interval=interval)

                pyautogui.typewrite(' ', interval=interval)

            except Exception as e:
                print('Exception For Typewriter: {}'.format(e))

        time.sleep(.2)

    def type_nonEnglish(self, text, space=None):

        # open the textfile
        text = text.strip()
        for ch in text:
            # type out the text
            subprocess.call(["xdotool", "getwindowfocus", "windowfocus", "--sync", "type", ch])
            # increase or decrease the time below to type slower or faster
            time.sleep(0.1)

    def typemail(self, word):
        """
        Type login and username in Form
        :param text:
        :return:
        """
        interval = random.uniform(0.1, 0.5)
        pyautogui.typewrite(word, interval=interval)

    def get_backspace_count(self, length):
        """
        Get backspace count for delete letter.
        :param length:
        :return:
        """
        refine_count.append(random.randint(0, length))
        del_count = random.choice(refine_count)
        refine_count.pop(-1)

        return del_count

    def keydown(self, key):
        """
        Down key
        :param key:
        :return:
        """
        pyautogui.keyDown(key)

    def keyup(self, key):
        """
        Release key
        :param key:
        :return:
        """
        pyautogui.keyUp(key)

    def keypress(self, keys):
        """
        Press key
        :param keys:
        :return:
        """
        pyautogui.press(keys)

    def hotkey(self, *args):
        pyautogui.hotkey(*args)

    def browser_addressbar(self):
        """
        get address bar
        :return:
        """

        pyautogui.hotkey('ALT', 'd')
        time.sleep(2)

    def minimize(self):
        """
        Minimize the Window
        :return: 
        """
        self.hotkey('ALT', 'SPACE')
        time.sleep(.5)
        self.keypress(['n'])

    def maximize(self):
        """
        Maximize the window
        :return: 
        """
        self.hotkey('ALT', 'SPACE')
        time.sleep(.5)
        self.keypress(['x'])

    def close(self):
        """
        Close the Window
        :return: 
        """
        self.hotkey('ALT', 'F4')
        time.sleep(.5)

    def tab_app(self):
        """
        Switch the app
        :return: 
        """
        self.hotkey('ALT', 'TAB')
        time.sleep(.5)

    def backward(self):
        """
        Backward on browser.
        :return: 
        """
        self.hotkey('ALT', 'LEFT')
        time.sleep(.5)

    def browser_open_tab(self):
        """
        Open new tab on Browser
        :return: 
        """
        self.hotkey('CTRL', 't')
        time.sleep(1)

    def browser_switch_tab(self, count=1):
        """
        Browse new tab
        :return: 
        """
        for i in range(0, count):
            self.hotkey('CTRL', 'TAB')
            time.sleep(2)

    def browser_close_tab(self):
        """
        Browse new tab
        :return: 
        """
        self.hotkey('CTRL', 'w')
        time.sleep(1)

keyboard = Keyboard()

if __name__ == '__main__':
    keyboard.type_nonEnglish('hello world')