# Using Keyboard module in Python
import keyboard

while True:
    if keyboard.is_pressed ('q'):
        print('Você pressionou uma tecla!')
        break