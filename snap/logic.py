from get_cards_on_hand import analize_hand
from state import analize_mana
from utilts.images import show_images


def game_logic():
    list_of_screens = [None, None, None]
    list_of_screens[0], list_of_screens[1], matches, count, cards_on_hand = analize_hand()
    list_of_screens[0], list_of_screens[2], matches = analize_mana(list_of_screens[0])
    show_images((list_of_screens), ["Screen", "Screenshot","Mana"])
