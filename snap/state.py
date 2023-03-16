import cv2
import numpy as np
import mss
import os
from utilts.locate import get_screenshot
from utilts.locate import cut_image
from utilts.images import show_images
from analizer.catcher import get_screen_and_screenshot
from analizer.catcher import draw_matches
from analizer.catcher import find_templates_on_screenshot
from settings import Settings

conifg = Settings()


def analize_mana(screen, screenshot):
    templates_dict = conifg.mana_pool_templates
    # convert only dict values to list
    templates = list(templates_dict.values())
    print(templates)
    # search templates on cutted screenshot
    matches = find_templates_on_screenshot(
        screenshot, "menu_templates", templates
    )
    draw_matches(screen, matches)
    return screen, screenshot, matches
