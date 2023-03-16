from get_cards_on_hand import analize_hand
from state import analize_mana
from utilts.images import show_images

def game_logic():
    screen, screenshot, matches, count, cards_on_hand = analize_hand()
    screen, screenshot, matches = analize_mana(screen, screenshot)
    show_images([screen, screenshot], ["Screen", "Screenshot"])