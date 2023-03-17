import cv2 as cv
import mss
import numpy as np
import time


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        return img


def cut_image(image, x, y, x1, y1):
    return np.array(image[y:y1, x:x1])


# find template on screenshot
# group rectangles and return list of matches
def find_template_on_screenshot(screenshot, template, threshold=0.9):
    template = cv.imread(template, cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    # For each match we draw a rectangle around it on our screenshot
    rects = []
    for pt in zip(*loc[::-1]):
        rects.append((pt[0], pt[1], w, h))

    rects, _ = cv.groupRectangles(rects, 1, 0.2)
    if len(rects) > 0:
        x, y, _, _ = rects[0]
        print(f"Found template at {x}, {y}")
        return x, y
    else:
        return None


# get match position and add 30 to y position
def get_match_position(match):
    x, y = match
    return (x, y + 30)


# use find_template_on_screenshot and get_match_position to get position of template on screenshot
def define_top_left_corner(template, name_of_template):
    match = None
    print(f"Searching for {name_of_template}...")
    # search for template until match is found each 1 second
    while match is None:
        screenshot = get_screenshot(
            {"top": 0, "left": 0, "width": 1920, "height": 1080}
        )
        match = find_template_on_screenshot(screenshot, template)
        time.sleep(1)
    if match is not None:
        position = get_match_position(match)
        print(f"Found {name_of_template} at {position}")
        return position
