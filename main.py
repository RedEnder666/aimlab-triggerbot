import time
from pynput.mouse import Button, Controller
import win32api
import pyautogui as pg

mouse = Controller()
min_color = (10, 140, 165)
max_color = (100, 255, 255)
m = mouse.position

def crosscolor():
    return pg.pixel(*m)

while True:
    cross = crosscolor()
    if cross[0] in range(min_color[0], max_color[0]) and \
    cross[1] in range(min_color[1], max_color[1]) and \
    cross[2] in range(min_color[2], max_color[2]):
        mouse.press(Button.left)
        mouse.release(Button.left)
        print(f"shot target with color {cross}")
        time.sleep(0.01)
    if win32api.GetKeyState(0x02)<0:
        m = mouse.position
        print('center is now at', m)
    time.sleep(0.001)
