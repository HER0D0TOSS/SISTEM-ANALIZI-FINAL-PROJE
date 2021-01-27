import curses
import numpy as np
import time
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

it = util.Iterator(board)
it.start()


servo_X = board.get_pin('d:10:p')
servo_Y = board.get_pin('d:11:p')

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(1)
screen.keypad(True)


while True:
    char = screen.getch()
    if char == ord('q'):
        break

    elif char == curses.KEY_LEFT:
            servo_X.write(0.200)
          

    elif char == curses.KEY_RIGHT:
        servo_X.write(0.900)
        
    elif char == curses.KEY_UP:
        servo_Y.write(0.200)
        
    elif char == curses.KEY_DOWN:
         servo_Y.write(0.900)