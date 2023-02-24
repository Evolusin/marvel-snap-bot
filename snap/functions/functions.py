import pyautogui
import time
from snap.logger.loger import log

def click_point(x, y, debug=False):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y, button="left")
    if debug:
        log.info(f"Klikam na {x} - {y}")
    time.sleep(0.5)