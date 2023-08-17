import serial
import time
import sound_runner
arduino = serial.Serial(port='COM10', baudrate=115200, timeout=0.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    print("wtf")
    r_val = write_read(str(sound_runner.red()))
    g_val = write_read(str(sound_runner.green()))
    b_val = write_read(str(sound_runner.blue()))
    print(r_val)
    print(g_val)
    print(b_val)
