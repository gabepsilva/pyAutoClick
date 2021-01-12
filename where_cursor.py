from pynput.mouse import Listener, Controller, Button
import pyautogui
import sys

from pynput.mouse import Button, Controller

mouse = Controller()

print('Press Ctrl-C to quit.')


try:  
  while True:
    
    positionStr = f'The current pointer position is {mouse.position}'
    print(positionStr, end='')
    print('\b'*len(positionStr), end='', flush=True)
except KeyboardInterrupt:
      print('\n')




try:  
  while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b'*len(positionStr), end='', flush=True)
except KeyboardInterrupt:
      print('\n')

