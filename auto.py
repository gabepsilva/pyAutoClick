from pynput.mouse import Listener, Controller, Button
import pyautogui
import time

mouse = Controller()

def click_wait_2(X, Y, wait=1):
  #mouse.position = (X, Y)
  #mouse.move(0, 0)
  #mouse.position = (X, Y)
  #mouse.move(0, 0)
  mouse.position = (X, Y)
  time.sleep(0.1)
  mouse.move(0, 0)
  time.sleep(0.1)

  mouse.click(Button.left)
  time.sleep(0.1)
  #mouse.press(Button.left)
  #mouse.release(Button.left)

  positionStr = f'The current pointer position is {mouse.position}'
  print(positionStr)

  time.sleep(wait)

while True:
  click_wait_2(1180, 213, wait=1) #get window focus

  click_wait_2(1180, 367) # activate btn

  click_wait_2(1180, 491) # click dev

  click_wait_2(1180, 367) # activate btn

  click_wait_2(1180, 491) # click in progress

  click_wait_2(1164, 813) # click fix version

  click_wait_2(1227, 534) # click 1.0

  click_wait_2(1180, 367) # activate btn


  click_wait_2(1180, 561, wait=2) # click done

  click_wait_2(1348, 42) # close tab

  click_wait_2(538, 81, wait=8) # refresh


  mouse.position = (1361, 400) # start new tab
  time.sleep(0.1)
  mouse.move(0, 0)
  time.sleep(0.1)

  mouse.click(Button.right)
  time.sleep(0.1)

  click_wait_2(1251, 411, wait=8) # open new tab
  click_wait_2(1251, 46, wait=8) # open click new tab

  #mouse.click(Button.left, 2)



