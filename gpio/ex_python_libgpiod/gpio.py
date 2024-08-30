#!/bin/python3

#DOC - https://pypi.org/project/gpiod/

import time
from gpiod.line import Direction, Value
import gpiod

GPIO_LINE = 29

with gpiod.request_lines(
    "/dev/gpiochip0",  
    consumer="toggle-example",  
    config={
        GPIO_LINE: gpiod.LineSettings(  
            direction=Direction.OUTPUT,  
            output_value=Value.INACTIVE  
        )
    },
) as request:
    while True:
        # Ativa o pino (define como alto)
        request.set_value(GPIO_LINE, Value.ACTIVE)
        print(f"Pino {GPIO_LINE} HIGH")
        time.sleep(1)

        # Desativa o pino (define como baixo)
        request.set_value(GPIO_LINE, Value.INACTIVE)
        print(f"Pino {GPIO_LINE} LOW")
        time.sleep(1)