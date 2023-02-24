from snap.logger.loger import warning


class SettingsMain:
    def __init__(self):
        self.img_dir = "templates/"
        # self.width, self.height = pyautogui.size()
        self.monitor = {
            "top": 50,
            "left": 1260,
            "width": 660,
            "height": 1000
        }

        # templates
        self.play = self.load("play")

        # variables for x/y positions and r - red (from RGB)
        x = "x"
        y = "y"
        r = "r"

        # check settings
        self.check_settings(self.monitor["width"], self.monitor["height"])

    def load(self, template):
        return f"{self.img_dir}{template}.png"

    def check_settings(self, x, y):
        if x != 1920 or y != 1080:
            warning(f"Change game loc display! Current settings - {x} / {y}")
            exit()
        else:
            return None
