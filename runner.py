import main
import keyboard  # using module keyboard

while True:
    print(main.runner())
    with open('readme.txt', 'w') as f:
        f.write(str(main.runner()))
    try:
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            break
        else:
            pass
    except:
        break