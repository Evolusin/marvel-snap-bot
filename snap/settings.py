import os
import json

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

class Settings:
    def __init__(self):
        self.monitor = {"top": 38, "left": 623, "width": 555, "height": 1030}
        self.templates = get_templates()
        self.deck = get_cards()