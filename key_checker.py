# Using Keyboard module in Python
import keyboard
import sys

while True:
    if keyboard.is_pressed ('q'):
        print('Você pressionou uma tecla!')
        break