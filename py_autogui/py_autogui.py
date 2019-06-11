#!/usr/local/bin python3
# -*- encoding: utf-8 -*-

'''
说明：

1. 前置条件
OS X上，执行pip3 install pyobjc-framework-Quartz, pip3 install pyobjc-core, pip3 install pyobjc
Linux上，执行pip3 install python3-xlib, apt-get intall scrot, apt-get install python3-tk, apt-get install python3-dev

2. 安装模块
pip install pyautogui

3. 使用模块
import pyautogui

4. 防故障操作
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True

5. python屏幕坐标是左上角开始为(0,0)


'''

import pyautogui
import time

pyautogui.PAUSE=1
pyautogui.FAILSAFE=True
# move mouse in 0.1 second
# pyautogui.moveTo(200, 324, duration=0.1)


width, height = pyautogui.size()
print("屏幕分辨率为：("+str(width)+", "+str(height)+")")



# print mouse position
print("press Ctrl+C to exit")
try:
    while True:
        x,y = pyautogui.position()
        pos_str = 'X: '+str(x).rjust(4)+" Y: "+str(y).rjust(4)
        print(pos_str, end='')
        time.sleep(1)
        print('\b' * len(pos_str), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')


