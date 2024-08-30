#!/bin/python3

#DOC - https://pypi.org/project/gpiod/

import time
import gpiod

GPIO_LINE = 29

chip = gpiod.Chip("/dev/gpiochip0")

line = chip.get_line(29)
line.request(consumer="toogle-example", type=gpiod.LINE_REQ_DIR_OUT)


try:
    while True:
        line.set_value(1) 
        time.sleep(1)      
        print(f"GPIO {GPIO_LINE} HIGH")
        line.set_value(0) 
        time.sleep(1)      
        print(f"GPIO {GPIO_LINE} LOW")
except KeyboardInterrupt:
    print("Interrompido pelo usuário")

finally:
    line.release() 