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
import binascii
import csv

last_received = 0.0

     

class SerialData(object):
    def __init__(self, port="COM6", init=50):
        self.Running = True
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
            self.thread = Thread(target=self.receiving, args=(self.ser,))
            self.thread.start()
        self.log_file = csv.writer(open("potentiostat_log.csv", "w"))

    def receiving(self, ser):
        global last_received
        nothing_count = 0
        while self.Running:
            raw_data = ser.read(ser.inWaiting())
            #print "Raw", binascii.hexlify(raw_data)
            if '\n' in raw_data and len(raw_data) >= 3:
                #print "Raw len", len(raw_data)            
                filtered_data = filter (lambda a: a != '' and len(a) == 2, raw_data.split('\n'))
                #print "Filtered", filtered_data

                if len(filtered_data) != 0:                
                    adc_value, = struct.unpack(">H", filtered_data[-1])
                    voltage = 3.3*adc_value / (2**10 - 1)
                    current = voltage / 39
                    #last_received = current
                    last_received = voltage
                    nothing_count = 0
                else:
                    last_received = 0.0
            else:
                if nothing_count > 1000:
                    last_received = 0.0
                nothing_count += 1
        
    def next(self):
        if not self.ser:
            return (random.randint(0, 100)) #return anything so we can test when Arduino isn't connected
        #return a float value or try a few times until we get one
        voltage = last_received
        try:
            self.log_file.writerow([time.time(), voltage])
            return float(voltage)
        except ValueError:
            print 'bogus data',raw_line
            time.sleep(.005)
        return 0.
    def __del__(self):
        self.log_file.close()
        if self.ser:
            self.ser.close()

if __name__=='__main__':
    s = SerialData(port="COM6")
    for i in range(500):
        time.sleep(.015)
        print s.next()
