import cv2
import numpy as np
import mss
import os
from settings import Settings


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


def cut_image(image, x, y, x1, y1):
    return np.array(image[y:y1, x:x1])


# put text in bottom left corner of screen with card count
def draw_card_count(screen, card_count):
    org = (10, 980)
    text = f"Cards on hand: {card_count}"
    cv2.putText(
        screen,
        str(text),
        org,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        3,
        cv2.LINE_AA,
    )
    cv2.putText(
        screen,
        str(text),
        org,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (124, 252, 0),
        2,
        cv2.LINE_AA,
    )


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        return img


def draw_matches(screen, matches, main_screen=True):
    # draw rectangles and text on screenshot
    for template, rects in matches.items():
        for rect in rects:
            pt = rect[0], rect[1]
            if main_screen:
                pt = (
                    pt[0],
                    pt[1] + 740,
                )  # add 740 to y position because we cut image
            cv2.rectangle(
                screen, pt, (pt[0] + rect[2], pt[1] + rect[3]), (0, 0, 255), 2
            )
            text = template.replace(".png", "")
            org = (pt[0], pt[1] + rect[3] + 20)
            cv2.putText(
                screen,
                text,
                org,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                3,
                cv2.LINE_AA,
            )
            cv2.putText(
                screen,
                text,
                org,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (124, 252, 0),
                2,
                cv2.LINE_AA,
            )


def show_images(images_list, titles_list):
    for image, title in zip(images_list, titles_list):
        cv2.imshow(title, image)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit(0)
    return True


# count not empty matches
def count_matches(matches):
    count = 0
    for _, rects in matches.items():
        count += len(rects)
    return count


def get_cards_on_hand():
    conifg = Settings()
    monitor = conifg.monitor
    templates = conifg.templates
    # get screenshot from monitor
    screen = get_screenshot(monitor)
    # create new screenshot from point (x, y) to (x1, y1)
    screenshot = cut_image(screen, 0, 740, 555, 900)
    # search templates on cutted screenshot
    matches = find_templates_on_screenshot(screenshot, templates)
    count = count_matches(matches)
    draw_card_count(screen, count)
    draw_matches(screen, matches)
    draw_matches(screenshot, matches, main_screen=False)

    show_images([screen, screenshot], ["Screen", "Screenshot"])
