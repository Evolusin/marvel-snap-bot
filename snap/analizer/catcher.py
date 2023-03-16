import cv2
import numpy as np
import mss
import os
from settings import Settings

conifg = Settings()


def find_templates_on_screenshot(screenshot, templates):
    img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    matches = {}
    for x in templates:
        template = cv2.imread(f"templates/{x}", cv2.IMREAD_GRAYSCALE)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        # Setting a threshold
        threshold = 0.5
        loc = np.where(res >= threshold)

        # For each match we draw a rectangle around it on our screenshot
        rects = []
        for pt in zip(*loc[::-1]):
            rects.append((pt[0], pt[1], template.shape[1], template.shape[0]))

        rects, _ = cv2.groupRectangles(rects, 1, 0.2)
        matches[x] = rects

    return matches
