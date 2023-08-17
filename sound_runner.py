import frequency_sound
import serial
import time
import requests


# arduino = serial.Serial(port='COM10', baudrate=115200, timeout=0.1)


def led():
    f = int(frequency_sound.sound_c())
    if 400 <= f < 484:
        r = 255
        g = 0
        b = 0
    elif 484 <= f < 508:
        r = 255
        g = 165
        b = 0
    elif 508 <= f < 526:
        r = 255
        g = 255
        b = 0
    elif 526 <= f < 606:
        r = 0
        g = 255
        b = 0
    elif 606 <= f < 668:
        r = 0
        g = 0
        b = 255
    elif 668 <= f < 720:
        r = 75
        g = 0
        b = 130
    elif 720 <= f < 800:
        r = 238
        g = 130
        b = 238
    else:
        r = 255
        g = 255
        b = 255
    return r, g, b


def red():
    r, g, b = led()
    return r


def blue():
    r, g, b = led()
    return b


def green():
    r, g, b = led()
    return g


# def write_read(x):
# arduino.write(bytes(x, 'utf-8'))
# time.sleep(0.05)
# data = arduino.readline()
# return data


while True:
    url = "http://192.168.166.39/"
    myobj = {'some-key': 'hey you!'}
    x = requests.post(url, json=myobj)
    # print the response text (the content of the requested file):
    print(x.text)
# f = int(frequency_sound.sound_c())
# frequency = write_read(str(f))
# print(frequency)
