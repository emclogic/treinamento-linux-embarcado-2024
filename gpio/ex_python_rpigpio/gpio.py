import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

GPIO_PIN = 29
GPIO.setup(GPIO_PIN, GPIO.OUT)

try:
    while True:

        print("Setting GPIO 29 to HIGH")
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        time.sleep(1)

        print("Setting GPIO 29 to LOW")
        GPIO.output(GPIO_PIN, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program exited cleanly")