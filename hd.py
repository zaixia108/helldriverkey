import os.path
import time
import keyboard
import mss
import cv2
import numpy as np
from EasYoloD import easyolo
import ctypes
import shutil

easyolo.init('onnxdml', False)
model = easyolo.Model()
model.load('hd.onnx', 0.3, 0.5, ['up', 'down', 'left', 'right'])

VK_CODE = {
    'w': 0x57,
    'a': 0x41,
    's': 0x53,
    'd': 0x44,
}


# pyinstaller 打包之后复制模型到外部
if os.path.exists('_internal'):
    shutil.copy('_internal/hd.onnx', 'hd.onnx')

def key_press(keys):
    """
    按下指定的按键
    :param key: 按键
    """
    key_map = {
        'up': 'w',
        'down': 's',
        'left': 'a',
        'right': 'd',
    }
    for key in keys:
        ctypes.windll.user32.keybd_event(VK_CODE[key_map[key[0]]], 0, 0, 0)
        time.sleep(0.02)
        ctypes.windll.user32.keybd_event(VK_CODE[key_map[key[0]]], 0, 2, 0)
        time.sleep(0.02)

def get_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 使用第一个监视器
        screenshot = sct.grab(monitor)
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGRA2BGR)
        return img

scr = get_screenshot()
w, h = scr.shape[1], scr.shape[0]
if w == 1920:
    y1 = 75
    y2 = 440
    x = 350
elif w == 2560:
    y1 = 100
    y2 = 600
    x = 400
elif w == 3840:
    y1 = 150
    y2 = 800
    x = 600
else:
    raise ValueError('Wrong width')

tar = scr[y1:y2, 50:x]
step = (y2 - y1)//7

def show_step(img, num: int) -> np.ndarray:
    """
    显示指定步数的图像
    :param num: 步数
    :return: 图像
    """
    if num < 1 or num > 7:
        raise ValueError('num must be in range [1, 7]')
    return img[(num-1)*step: num * step, 0:350]

def push_key(num: int):
    """
    按下指定步数的按键
    :param num: 步数
    """
    print(num)
    img = get_screenshot()
    if num < 1 or num > 7:
        raise ValueError('num must be in range [1, 7]')
    show_img = img[y1:y2, 50:x]
    img = show_step(show_img, num)
    # cv2.imshow('step', img)
    # cv2.waitKey(0)
    result = model.detect(img)
    up = result.get('up', [])
    down = result.get('down', [])
    left = result.get('left', [])
    right = result.get('right', [])
    key_list = []
    for k in up:
        key_list.append(('up', k['center']))
    for k in down:
        key_list.append(('down', k['center']))
    for k in left:
        key_list.append(('left', k['center']))
    for k in right:
        key_list.append(('right', k['center']))
    #sort by center x
    print(key_list)
    key_list.sort(key=lambda x: x[1][0])
    # key_down(key_list)
    key_press(key_list)




if __name__ == '__main__':
    # img = cv2.imread('2560/img_1.png')
    # push_key(2, img)
    keyboard.add_hotkey('ctrl+1', lambda: push_key(1))
    keyboard.add_hotkey('ctrl+2', lambda: push_key(2))
    keyboard.add_hotkey('ctrl+3', lambda: push_key(3))
    keyboard.add_hotkey('ctrl+4', lambda: push_key(4))
    keyboard.add_hotkey('ctrl+5', lambda: push_key(5))
    keyboard.add_hotkey('ctrl+6', lambda: push_key(6))
    keyboard.add_hotkey('ctrl+7', lambda: push_key(7))
    keyboard.wait()
