from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')

it = util.Iterator(board)
it.start()

ServoHorizontal_Pin = board.get_pin('d:10:p')
ServoVertical_Pin = board.get_pin('d:11:p')


Pin_X= board.get_pin('a:0:i')
Pin_Y = board.get_pin('a:2:i')



while True:
    time.sleep(0.5)

    X_axis = Pin_X.read()
    Y_axis = Pin_Y.read()
    



    print("-------------------------------------")
    print("yatay eksen: ",X_axis)
    print("Dikey eksen: ", Y_axis)
    #print(HesapVertical)
    print("-------------------------------------")

    ServoHorizontal_Pin.write(X_axis)
    ServoVertical_Pin.write(Y_axis)
