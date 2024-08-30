#!/bin/python3

#DOC - https://pypi.org/project/gpiod/

import gpiod
import time

chip = gpiod.Chip('/dev/gpiochip0')

GPIO_NUMBER = 29

line = chip.get_line(GPIO_NUMBER)

# Configura a linha para ser uma saída e inicializa em estado baixo (apagado)
config = gpiod.LineRequest()
config.consumer = "gpio_toogle"
config.request_type = gpiod.LINE_REQ_DIR_OUT
line.request(config, default_val=0)

try:
    while True:
        line.set_value(1) 
        print(f"gpio {GPIO_NUMBER} - HIGH")
        time.sleep(1)      
        line.set_value(0) 
        print(f"gpio {GPIO_NUMBER} - LOW")
        time.sleep(1)      
except KeyboardInterrupt:
    print("Interrompido pelo usuário")

finally:
    line.release() 