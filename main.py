from PIL import Image

characters = "@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-`"


def convert_pixel(px):
  return px[0] + px[1] + px[2] / 3


def make_ascii_art(im):
  for y in range(0, im.height):
    row = ''
    for x in range(0, im.width):
      px = im.getpixel((x, y))
      brightness = convert_pixel(px)

      proportion = brightness / 256
      index = round(len(characters) * proportion)
      if (index >= len(characters)):
        index = len(characters) - 1

      if (index < 0):
        index = 0

      row += characters[index] * 3

    print(row)


def open_image(file_name='blackbird.jpg'):
  im = Image.open(file_name)
  width = im.width
  height = im.height

  newWidth = 70
  newHeight = round(newWidth * (height / width))
  return im.resize((newWidth, newHeight))


def input_image():
  file_name = input('Input file name.')


def main():
  im = open_image()
  make_ascii_art(im)


if __name__ == "__main__":
  main()
