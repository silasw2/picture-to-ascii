from PIL import Image
import argparse
import numpy as np


def main(picturePath, width, height, simple):
    try:
        image = Image.open(picturePath).convert("RGB")
    except Exception as e:
        print("error:" + e +
              "\nCould not open the picture, is the file a image filetype?")

    image = image.resize((width, height))

    asciiPicture = ""

    # Note that the quotation mark character is escaped yet still only counts as one character
    if simple:
        densityArr = " .:-=+*#%@"
    else:
        densityArr = " .'`^\"\,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    imageArr = np.array(image)
    for i in range(0, len(imageArr)):
        for j in range(0, len(imageArr[0])):
            asciiPicture += getPixelAscii(imageArr[i][j], densityArr)
        asciiPicture += "\n"

    print(asciiPicture)


def getPixelAscii(rgb: np.ndarray, densityArr: list):
    index = int((rgb.sum()/3)/(255/(len(densityArr) - 1)))
    return densityArr[index]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Ascii Art Generator',
        description='Creates an Ascii art representation of an image',
        epilog='')
    parser.add_argument("filename",
                        help="filepath for the picture you would like to convert")
    parser.add_argument("--width", default=80, type=int,
                        help="the width for the resulting image, it is best if this is some integer divisor of the width")
    parser.add_argument("--height", default=80, type=int,
                        help="the height for the resulting image, it is best if this is some integer divisor of the height")
    parser.add_argument('--simple', action=argparse.BooleanOptionalAction,
                        help="whether to use simple ascii characters, or complex ascii characters")
    args = parser.parse_args()
    main(args.filename, args.width, args.height,
         args.simple)
