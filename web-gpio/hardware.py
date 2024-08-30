import gpiod

GPIO_LINE = 29

chip = gpiod.Chip("/dev/gpiochip0")

lines = chip.get_line(29)
lines.request(consumer="toogle-example", type=gpiod.LINE_REQ_DIR_OUT)


def gpio_on():
    lines.set_value(1)
    print(f"GPIO {GPIO_LINE} HIGH")

def gpio_off():
    lines.set_value(0)
    print(f"GPIO {GPIO_LINE} LOW")