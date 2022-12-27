class Cards:
    def __init__(self):
        self.cards_oh = 4
        self.positions = {1: 1344, 2: 1426, 3: 1548, 4: 1646}

    def add_card(self):
        self.cards_oh += 1

    def remove_card(self):
        self.cards_oh -= 1

    def cards_status(self):
        if self.cards_oh ==4:
            self.positions = {1: 1344, 2: 1426, 3: 1548, 4: 1646}
        elif self.cards_oh == 3:
            self.positions = {1: 1344, 2: 1426, 3: 1548}


