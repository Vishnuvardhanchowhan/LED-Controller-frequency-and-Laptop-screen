import numpy as np
import cv2
import pyautogui


def scale(img,per):
    scale_percent = per  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)  # scaling width of main image
    height = int(img.shape[0] * scale_percent / 100)  # scaling height of main image
    dim = (width, height) # dimensions of scaled image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  # resizing night image
    return img


def runner():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    scale(image, 30)
    [b,g,r] = [int(np.average(image[:, :, 0])), int(np.average(image[:, :, 1])), int(np.average(image[:, :, 2]))]
    cv2.imwrite("image.png", image)
    return b,g,r


def red():
    b,g,r=runner()
    return r


def blue():
    b,g,r=runner()
    return b


def green():
    b,g,r=runner()
    return g
