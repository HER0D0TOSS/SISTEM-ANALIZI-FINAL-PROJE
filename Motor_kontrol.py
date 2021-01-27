import curses


from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB3')

it = util.Iterator(board)
it.start()

mtrPWM1 = board.get_pin('d:3:p')
mtrPWM2 = board.get_pin('d:9:p')

mtrPWM1.write(0.3)
mtrPWM2.write(0.3)
mtrPin1 = board.get_pin('d:4:o')
mtrPin2 = board.get_pin('d:5:o')
mtrPin3 = board.get_pin('d:6:o')
mtrPin4 = board.get_pin('d:7:o')


screen =curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)


try:
    while True:
        char =screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            mtrPin1.write(0)
            mtrPin2.write(1)

            mtrPin3.write(0)
            mtrPin4.write(1)

            
        elif char == curses.KEY_DOWN:

            
            mtrPin1.write(1)
            mtrPin2.write(0)

            mtrPin3.write(1)
            mtrPin4.write(0)

        elif char == curses.KEY_RIGHT:
            mtrPin1.write(0)
            mtrPin2.write(1)

            mtrPin3.write(1)
            mtrPin4.write(0)

        elif char == curses.KEY_LEFT:
            mtrPin1.write(1)
            mtrPin2.write(0)

            mtrPin3.write(0)
            mtrPin4.write(1)
except SyntaxError:
    print("hata")
