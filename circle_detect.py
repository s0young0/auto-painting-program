import cv2
import numpy as np

class circle_detect(object):
    def __init__(self, filename, label):
        self.file = ''
        self.start(filename, label)

    def start(self, file_name):
        img = cv2.imread(file_name)
        if img is None:
            print('====================== error - not found : ' + file_name + '======================')
            return
        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 200,
                           param1=200, param2=40, minRadius=10, maxRadius=65)
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
