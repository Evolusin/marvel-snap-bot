import os


def get_templates():
    return os.listdir("templates")


class Settings:
    def __init__(self):
        self.monitor = {"top": 38, "left": 623, "width": 555, "height": 1030}
        self.templates = get_templates()
