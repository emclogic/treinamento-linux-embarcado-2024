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

message = "Hello, Serial!\n"
ser.write(message.encode('utf-8'))
print(f"Sent: {message.strip()}")

time.sleep(1)

# Read from the serial port
response = ser.read(100)  # Adjust the number of bytes to read
print(f"Received: {response.decode('utf-8').strip()}")

ser.close()
print(f"Closed serial port {PORT}")
