#!/bin/env python3

from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
leitorRfid = SimpleMFRC522()

try:
    while True:
        print("Aproxime o cartao da leitora...")
        id, text = leitorRfid.read()
        print("ID do cartao: ", id)
        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    raise
