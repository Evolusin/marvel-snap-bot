import pyautogui
import objc
import time

from snap.logger.loger import log, debug
from snap.analizer.catcher import needle_position
from snap.functions.functions import click_point

time.sleep(2)
debug(pyautogui.size())
play = needle_position('templates/play.png')
debug(play)
click_point(play[0],play[1])