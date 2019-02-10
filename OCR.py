import os
import ImageCleaner
import pytesseract

os.chdir("C:\\Users\\Daniel Vinton\\Desktop\\Programming\\CatherineOCR")
print(os.getcwd())

iclean = ImageCleaner.ImageCleaner("test1.png", "test1cleaned2.png")

processedImg = iclean.getCleanedImg(img)
iclean.writeImage(processedImg)

result = pytesseract.image_to_string(processedImg, lang="eng")


