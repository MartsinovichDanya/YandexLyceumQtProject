import numpy as np
from PIL import Image


def neg(im):
    img = np.asarray(Image.open(im.name))
    im.backup = img
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    nr = 255 - r
    ng = 255 - g
    nb = 255 - b
    Image.fromarray(np.uint8(np.stack((nr, ng, nb), axis=-1))).save(im.name)


def back(im):
    Image.fromarray(im.backup).save(im.name)
