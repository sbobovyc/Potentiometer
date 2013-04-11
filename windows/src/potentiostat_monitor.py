"""
Listen to serial, return most recent numeric values
Lots of help from here:
http://stackoverflow.com/questions/1093598/pyserial-how-to-read-last-line-sent-from-serial-device
https://github.com/jonleung/AccelPlot/blob/master/plot/Archive/Arduino_Monitorz.py
"""
from threading import Thread
import time
import serial
import random
import struct

last_received = 0.0
def receiving(ser):
    global last_received
    while True:
        data = ser.read(size=2)                
        adc_value, = struct.unpack(">H", data)
        last_received = 3.3*adc_value / (2**10 - 1) 

class SerialData(object):
    def __init__(self, port="COM6", init=50):
        try:
            self.ser = ser = serial.Serial(
                port, 9600, timeout=2, parity=serial.PARITY_NONE,
                        bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,
                        rtscts=1
            )
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
        else:
            Thread(target=receiving, args=(self.ser,)).start()
        
    def next(self):
        if not self.ser:
            return (random.randint(0, 100)) #return anything so we can test when Arduino isn't connected
        #return a float value or try a few times until we get one
        voltage = last_received
        try:
            return float(voltage)
        except ValueError:
            print 'bogus data',raw_line
            time.sleep(.005)
        return 0.
    def __del__(self):
        if self.ser:
            self.ser.close()

if __name__=='__main__':
    s = SerialData(port="COM6")
    for i in range(500):
        time.sleep(.015)
        print s.next()
