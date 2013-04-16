import serial
import struct
import sys
import signal
import os
import argparse
import time
import binascii

def run(port=0, filepath=None, verbose=False):
    # Make Ctrl+Break raise KeyboardInterrupt, like Python's default Ctrl+C (SIGINT) behavior.
    signal.signal(signal.SIGBREAK, signal.default_int_handler)    
    ser = serial.Serial(port, 9600, timeout=2, parity=serial.PARITY_NONE,
                        bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,
                        rtscts=1)
    print "Reading from serial..."
    recordList = []

    start = time.clock()

    #TODO fix missing the first reading
    while True:
        try:        
            raw_data = ser.read(ser.inWaiting())            
            if '\n' in raw_data and len(raw_data) >= 3:                            
                print "Raw", binascii.hexlify(raw_data)
                print "Raw len", len(raw_data)            
                filtered_data = filter (lambda a: a != '' and len(a) == 2, raw_data.split('\n'))
                print "Filtered", filtered_data

                if len(filtered_data) != 0:                
                    adc_value, = struct.unpack(">H", filtered_data[-1])
                    print 3.3*adc_value / (2**10 - 1)
                    print
            
        except KeyboardInterrupt:
            end = time.clock()
            print "Read in %.2gs" % (end-start)

            if filepath != None:
                user_input = raw_input("Do you want to save? [y/n]:")
                if user_input.lower() == "y":
                    if recordList.getSize() > 0:
                        print "Writing ", filepath
                        with open(filepath, "w") as file:
                            file.write(recordList.getCSV())
                    else:
                        print "No records to write."
            sys.exit()
        except struct.error:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program reads serial output of MPSS Solar Replayer HW:1.0 FW:1.0')
    parser.add_argument('--port', help='Serial port', nargs='?', default=0, required=False)    
    parser.add_argument('-f','--file', help='name of output csv file', default='output.csv', required=False)
    parser.add_argument('-v','--verbose', help='print out data during serial capture', action='store_true', required=False)

    args = parser.parse_args()

    filepath = os.path.abspath(args.file)
    run(args.port)
