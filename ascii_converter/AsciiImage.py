from numpy import ndarray
from numpy import array
from PIL import Image

class AsciiImage:
    imageArr: ndarray

    def __init__(self, imageArr: ndarray):
        self.imageArr = imageArr
    
    @classmethod
    def fromPillowImage(cls, image: Image.Image, width: int = None, height: int = None):
        if width and height:
            image = image.resize((width, height))
        return cls(array(image))

    def getPixelAscii(self, rgb: ndarray, densityArr: list) -> str:
        index = int((rgb.sum()/3)/(255/(len(densityArr) - 1)))
        return densityArr[index]
    
    def convertImageToAscii(self, simple: bool = True) -> str:
        asciiPicture = ""
        if simple:
            densityArr = " .:-=+*#%@"
        else:
            densityArr = " .'`^\"\,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

        for row in self.imageArr:
            for pixel in row:
                asciiPicture += self.getPixelAscii(pixel, densityArr)
            asciiPicture += "\n"
        

        return asciiPicture[:-1] # remove last new line