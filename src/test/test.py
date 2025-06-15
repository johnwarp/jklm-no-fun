import keyboard
import threading
import time

for _ in range(50):
    print('waiting for key press')
    keyboard.wait()
    print("event")