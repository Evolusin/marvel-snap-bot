import json


class Card:
    def __init__(self, name, cost, power, template_name):
        self.name = name
        self.cost = cost
        self.power = power
        self.template_name = template_name

    def to_dict(self):
        return {
            "name": self.name,
            "cost": self.cost,
            "power": self.power,
            "template_name": self.template_name,
        }


# def create json file with all cards
def create_cards_json():
    cards = [
        Card("Hawkeye", 1, 1, "hawkeye.png"),
        Card("Misty Knight", 1, 2, "misty.png"),
        Card("Quicksilver", 1, 2, "quicksilver.png"),
        Card("Medusa", 2, 2, "medusa.png"),
        Card("Star-Lord", 2, 2, "starlord.png"),
        Card("Sentinel", 2, 3, "sentinel.png"),
        Card("Shocker", 2, 3, "shocker.png"),
        Card("Mister Fantastic", 3, 2, "misterf.png"),
        Card("Punisher", 3, 2, "punisher.png"),
        Card("Cyclops", 3, 4, "cyclops.png"),
        Card("Jessica Jones", 4, 4, "jessica.png"),
        Card("Kazar", 4, 4, "kazar.png"),
        Card("Thing", 4, 5, "thing.png"),
        Card("Iron Man", 5, 0, "ironman.png"),
        Card("Abomination", 5, 9, "abomination.png"),
        Card("Hulk", 6, 12, "hulk.png"),
    ]
    with open("deck.json", "w") as f:
        json.dump([card.to_dict() for card in cards], f)
