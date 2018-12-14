from PIL import Image
import random


def noise(im):
    img = Image.open(im.name)
    im.backup = Image.open(im.name)
    pix = img.load()
    x, y = img.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            rand = random.randint(-40, 40)
            r, g, b = r + rand, g + rand, b + rand
            pix[i, j] = r, g, b
    img.save(im.name)


def back(im):
    im.backup.save(im.name)
