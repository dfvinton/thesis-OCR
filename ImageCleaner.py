# get and clean image
import cv2
import numpy as np


class ImageCleaner:
    def __init__(self, inputFile, outputFile):
        self.inputfile = inputFile
        self.outputfile = outputFile

    def readImage(self):
        img = cv2.imread(self.inputfile, cv2.IMREAD_GRAYSCALE)

        return img

    def writeImage(self, img):
        cv2.imwrite(self.outputfile, img)

    # resize to 300 dpi, increase contrast, erode noise, normal blur (commented out)
    def getCleanedImg(self, img):
        img = self.readImage()

        img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        img = cv2.multiply(img, 1.2)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.erode(img, kernel, iterations=1)

        #img = cv2.GaussianBlur(img, (5, 5), 0)
        return img
