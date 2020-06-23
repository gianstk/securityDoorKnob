import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('/dev/tty.usbmodem14101', 9600)



while 1:                                      #infinite loop
                                      #waits until user enters data
    input_data = input("you entered: ")          #prints the data for confirmation
    
    if (input_data == '1'):                   #if the entered data is 1 
        arduino.write(b'1')             #send 1 to arduino
        print ("LED ON")
       
    
    if (input_data == '0'):                   #if the entered data is 0
        arduino.write(b'0')             #send 0 to arduino 
        print ("LED OFF")

time.sleep(2) #waiting the initialization...

onOffFunction()