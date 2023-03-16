import os
import json
from utilts.locate import define_top_left_corner

# load deck.json and get all templates from it. Pack them into a list
def get_templates():
    with open("deck.json", "r") as f:
        cards = json.load(f)
    templates = []
    for card in cards:
        templates.append(card["template_name"])
    return templates


# load deck.json and get all cards from it. Pack them into a list
def get_cards():
    with open("deck.json", "r") as f:
        deck = json.load(f)
    return deck


# get all templates from menu_templates folder that beggin with "mana_" and create dict
# with mana cost as key and template name as value
def get_mana_pool_templates():
    mana_pool_templates = {}
    for file in os.listdir("menu_templates"):
        if file.startswith("mana_"):
            mana_pool_templates[file[5]] = file
    return mana_pool_templates

# get all templates from menu_templates folder that beggin with "turn_" and create dict
# with turn as key and template name as value
def get_turn_templates():
    turn_templates = {}
    for file in os.listdir("menu_templates"):
        if file.startswith("turn_"):
            turn_templates[file[5]] = file
    return turn_templates



class Settings:
    def __init__(self):
        self.templates = get_templates()
        self.deck = get_cards()
        self.mana_pool_templates = get_mana_pool_templates()
        self.turn_templates = get_turn_templates()
        self.end_turn_template = "menu_templates/end_turn.png"
        self.game_window = "menu_templates/game_window.png"
        
    def get_monitor(self):
        if not hasattr(self, "monitor"):
            self.define_monitor()
        return self.monitor
        
    def define_monitor(self):
        left, top = define_top_left_corner(self.game_window, "Game window")
        self.monitor = {"top": top, "left": left, "width": 555, "height": 1000}
        
    