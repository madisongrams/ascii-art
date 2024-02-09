from PIL import Image

characters = " .:-=+*#%@"

def convert_pixel(px):
  return 0.2125 * px[0] + 0.7154 * px[1] + 0.0721 * px[2]


def get_character(x, y, im):
  brightness_sum = 0
  for px in range(x, x + 2):
    for py in range(y, y + 3):
      if (px > im.width - 1):
        px = im.width - 1
      if (py > im.height - 1):
        py = im.height - 1
      pixel = im.getpixel((px, py))
      brightness_sum += convert_pixel(pixel)

  brightness_sum /= 6
  proportion = brightness_sum / 255
  index = round(len(characters) * proportion)

  if (index >= len(characters)):
    index = len(characters) - 1

  if (index < 0):
    index = 0

  return characters[index]


def make_ascii_art(im):
  # we will convert every group of 6 pixels into one character
  for y in range(0, im.height, 3):
    row = ''
    for x in range(0, im.width, 2):
      row += get_character(x, y, im)

    print(row)


def open_image(file_name='man.jpg'):
  im = Image.open(file_name)
  width = im.width
  height = im.height
  newWidth = 300
  newHeight = round(newWidth * (height / width))
  return im.resize((newWidth, newHeight))


def input_image():
  file_name = input('Input file name.')


def main():
  im = open_image()
  make_ascii_art(im)


if __name__ == "__main__":
  main()
