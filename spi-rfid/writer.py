#!/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitorRfid = SimpleMFRC522()

def main():
    try:
        text = "Treinamento Embarcados"
        print("Aproxime a tag a ser gravada.")
        leitorRfid.write(text)
        print("Gravada!")

    except KeyboardInterrupt:
        GPIO.cleanup()
        raise

if __name__ == "__main__":
    main()
