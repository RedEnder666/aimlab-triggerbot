import time
from pynput.mouse import Button, Controller
import pyautogui as pg

mouse = Controller()
min_color = (10, 140, 165)
max_color = (85, 255, 255)

def crosscolor():
    m = mouse.position
    return pg.pixel(*m)

while True:
    cross = crosscolor()
    if cross[0] in range(min_color[0], max_color[0]) and \
    cross[1] in range(min_color[1], max_color[1]) and \
    cross[2] in range(min_color[2], max_color[2]):
        mouse.press(Button.left)
        mouse.release(Button.left)
        print(f"shot target with color {cross}")
        time.sleep(0.1)
