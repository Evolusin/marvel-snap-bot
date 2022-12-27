import pyautogui
import objc
import time

from loger import log, debug
from catcher import needle_position
from functions import click_point

time.sleep(2)
debug(pyautogui.size())
play = needle_position('templates/play.png')
debug(play)
click_point(play[0],play[1])