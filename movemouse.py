import pyautogui
import random
import time

def move_mouse_forever():
    screenWidth, screenHeight = pyautogui.size()  # 屏幕尺寸
    while True:
        moveX=random.randint(screenWidth/2,screenWidth)
        moveY = random.randint(0, screenWidth/2)
        print("target position is ",moveX,",",moveY)
        pyautogui.moveTo(x=moveX,y=moveY,duration=1)
        print("current position is:",pyautogui.position())
        time.sleep(30)#暂停时间30s

if __name__ == '__main__':
    move_mouse_forever()