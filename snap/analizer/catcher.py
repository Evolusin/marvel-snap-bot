from PIL import ImageGrab, Image
import cv2 as cv
import numpy as np
import mss


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        return img


class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path=None, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
        self.needle_img = cv.cvtColor(self.needle_img, cv.COLOR_BGR2BGRA)
        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, debug_mode = False, threshold=0.7):
        # run the OpenCV algorithm
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        # Apply group rectangles.
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(
            rectangles, groupThreshold=1, eps=0.5
        )
        # Record screen and show it
        for (x, y, w, h) in rectangles:
            if debug_mode:
                points =[]
                line_type = cv.LINE_4
                line_color = (0, 255, 0)
                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, 
                             lineType=line_type, thickness=2)
        if debug_mode:
            # Show the screen
            haystack_img = cv.resize(haystack_img, (960, 540))
            cv.imshow('test', haystack_img)
        for (x, y, w, h) in rectangles:
            return x,y,w,h
        
def needle_position(img_needle):
    """
    Anlizes screen and returns img_needle position
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot({"top": 0,
            "left": 0,
            "width": 1920,
            "height": 1080})
    points = login_vision.find(screen, debug_mode=False)
    if points:
        x, y, w, h = points
        x = x + (w / 2)
        y = y + (h / 2)
        points = (x, y)
        return points
    else:
        return None