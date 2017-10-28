import serial
import time

ser = serial.Serial('COM3', 9600, timeout=0)

while 1:
        if "dec" in  ser.readline():
            print(ser.readline()[11:-4])
        time.sleep(1)
    