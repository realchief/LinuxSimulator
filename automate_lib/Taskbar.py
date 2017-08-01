#!/usr/bin/python


from __future__ import print_function

from baseFunctions import *
from web import *
from datetime import datetime
import logging
from winlaunch import *

logging.basicConfig(level=logging.INFO, filename='auto-simulator.txt')


def write_letters():
    """
    Random write the letters in wordpad.
    :return: 
    """
    print('write letters')
    logging.info("Office Write_letters function => write letters.\n")

    time.sleep(3)
    scrapy_content_newsurl()
    time.sleep(3)
    scroll_mouse(4, sensivity=250)
    time.sleep(1)
    scroll_mouse(4, sensivity=-220)

    time.sleep(3)

    scroll_mouse(4, sensivity=250)
    time.sleep(1)
    scroll_mouse(4, sensivity=-220)
    time.sleep(3)


class LibreOffice():

    def _init__(self):
        print('LibreOffice')

    def start_office(self):
        """
        Start libreoffice application
        :return: 
        """
        keyboard.typewrite('libreoffice')
        time.sleep(2)
        keyboard.hotkey('ENTER')
        time.sleep(3)
        keyboard.hotkey('ALT', 'D')
        time.sleep(3)

    def write_letters(self):
        """
        Random write the letters in word pad.
        :return: 
        """
        print('write letters')
        logging.info("Office Write_letters function => write letters.\n")

        time.sleep(3)
        scrapy_content_newsurl()
        time.sleep(3)
        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)

        time.sleep(3)

        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)
        time.sleep(3)

    def close_save(self):
        """
        Close writer and save to file.
        :return: 
        """

        keyboard.hotkey('CTRL', 's')
        time.sleep(3)
        filename = 'test-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        keyboard.typewrite(filename)
        time.sleep(2)
        keyboard.hotkey('ENTER')
        time.sleep(3)
        keyboard.hotkey('ALT', 'F4')


libreoffice = LibreOffice()

if __name__ == '__main__':

    time.sleep(3)
    search_app()
    libreoffice.start_office()
    libreoffice.write_letters()
    libreoffice.close_save()