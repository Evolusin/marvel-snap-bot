from get_cards_on_hand import analize_hand
from get_cards_on_hand import show_images

def game_logic():
    screen, screenshot, matches, count, cards_on_hand = analize_hand()
    show_images([screen, screenshot], ["Screen", "Screenshot"])