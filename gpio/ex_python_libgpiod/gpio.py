#!/bin/python3

#DOC - https://pypi.org/project/gpiod/

import time
import gpiod

GPIO_LINE = 29

chip = gpiod.Chip("/dev/gpiochip0")

lines = chip.get_line(29)
lines.request(consumer="toogle-example", type=gpiod.LINE_REQ_DIR_OUT)

while True:

    lines.set_value(1)
    print(f"GPIO {GPIO_LINE} HIGH")
    time.sleep(1)

    lines.set_value(0)
    print(f"GPIO {GPIO_LINE} LOW")
    time.sleep(1)
