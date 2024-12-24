from PIL import Image
import argparse
import numpy as np
from ascii_converter import AsciiImage


def main(picturePath, width, height, simple):
    try:
        image = AsciiImage.fromPillowImage(Image.open(picturePath).convert("RGB"))
    except Exception as e:
        print("error:" + e +
              "\nCould not open the picture, is the file a image filetype?")

    print(image.convertImageToAscii(simple=simple))


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
