#!/bin/python3

import serial
import time

PORT = '/dev/ttyS0'   
BAUDRATE = 115200     
TIMEOUT = 1           

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
    print(f"Opened serial port {PORT} at {BAUDRATE} baud")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

message = "HelloWorld, Serial in Python!\n"
ser.write(message.encode('utf-8'))
print(f"Sent: {message.strip()}")

ser.close()
print(f"Closed serial port {PORT}")

