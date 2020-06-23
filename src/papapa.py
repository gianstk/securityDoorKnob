
import pyfirmata
print("test0")
board = pyfirmata.Arduino('/dev/tty.usbmodem14101')
print("test1")
it = pyfirmata.util.Iterator(board)
it.start()

print("test2")

led_pin = board.get_pin('d:6:o')

print("test3")

while True:
    print("test4")
    led_pin.write(0)
    board.pass_time(1)        
    led_pin.write(1)
    board.pass_time(1)
    print("test5")

    
board.exit()