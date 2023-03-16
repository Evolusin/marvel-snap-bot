import cv2
import numpy as np
import mss
import os
from utilts.locate import get_screenshot
from utilts.locate import cut_image
from utilts.images import show_images
from analizer.catcher import find_templates_on_screenshot
from settings import Settings

conifg = Settings()