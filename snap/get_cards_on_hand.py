import cv2
import numpy as np
import mss
import os
from analizer.catcher import find_templates_on_screenshot
from analizer.catcher import count_matches
from analizer.catcher import get_screen_and_screenshot
from settings import Settings

conifg = Settings()


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





def analize_hand():
    templates = conifg.templates
    screen, screenshot = get_screen_and_screenshot(0, 740, 555, 900)
    # search templates on cutted screenshot
    matches = find_templates_on_screenshot(screenshot, 'card_templates',templates)
    count = count_matches(matches)

    # draw card count and matches on screen
    draw_card_count(screen, count)
    draw_matches(screen, matches)
    draw_matches(screenshot, matches, main_screen=False)
    cards_on_hand = get_cards_on_hand(matches)
    return screen, screenshot, matches, count, cards_on_hand


# get information about cards on hand from deck and matches. Deck comes from config
def get_cards_on_hand(matches):
    deck = conifg.deck
    cards = []
    for template, rects in matches.items():
        for rect in rects:
            for card in deck:
                if card["template_name"] == template:
                    # append card name to cards list
                    cards.append(card["name"])
    return cards
