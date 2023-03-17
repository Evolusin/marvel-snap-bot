import cv2
import numpy as np
import mss
import os
from settings import Settings

conifg = Settings()


def find_templates_on_screenshot(
    screen, path_for_templates, templates, threshold=0.5
):
    img = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    matches = {}
    for x in templates:
        template = cv2.imread(
            f"templates/{path_for_templates}/{x}", cv2.IMREAD_GRAYSCALE
        )
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)

        # For each match we draw a rectangle around it on our screenshot
        rects = []
        for pt in zip(*loc[::-1]):
            rects.append((pt[0], pt[1], template.shape[1], template.shape[0]))

        rects, _ = cv2.groupRectangles(rects, 1, 0.2)
        matches[x] = rects

    return matches


# count not empty matches
def count_matches(matches):
    count = 0
    for _, rects in matches.items():
        count += len(rects)
    return count


def get_screen_and_screenshot(x, y, x1, y1):
    monitor = conifg.get_monitor()
    # get screenshot from monitor
    screen = get_screenshot(monitor)
    # create new screenshot from point (x, y) to (x1, y1)
    screenshot = cut_image(screen, x, y, x1, y1)
    return screen, screenshot


def get_and_cut_screenshot(x, y, x1, y1):
    monitor = conifg.get_monitor()
    # get screenshot from monitor
    screen = get_screenshot(monitor)
    # create new screenshot from point (x, y) to (x1, y1)
    screenshot = cut_image(screen, x, y, x1, y1)
    return screenshot


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        return img


def cut_image(image, x, y, x1, y1):
    return np.array(image[y:y1, x:x1])


# write a function that draws matches on screen.
# Parameters: screen, matches
def draw_matches(screen, matches, x_offset=0, y_offset=0):
    for template, rects in matches.items():
        for x, y, w, h in rects:
            text = template.replace(".png", "")
            cv2.rectangle(
                screen,
                (x + x_offset, y + y_offset),
                (x + w + x_offset, y + h + y_offset),
                (0, 0, 255),
                2,
            )
            cv2.putText(
                screen,
                text,
                (x + x_offset, y + y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                3,
                cv2.LINE_AA,
            )
            cv2.putText(
                screen,
                text,
                (x + x_offset, y + y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (124, 252, 0),
                2,
                cv2.LINE_AA,
            )
    return screen
