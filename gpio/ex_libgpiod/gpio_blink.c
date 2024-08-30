// Docs on: https://libgpiod.readthedocs.io/en/latest/

#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define GPIO_CHIP "/dev/gpiochip0"
#define GPIO_LINE 29
#define SLEEP_TIME 1

int main() {
    struct gpiod_chip *chip;
    struct gpiod_line *line;
    int ret;

    chip = gpiod_chip_open(GPIO_CHIP);
    if (!chip) {
        perror("Failed to open GPIO chip");
        return 1;
    }

    line = gpiod_chip_get_line(chip, GPIO_LINE);
    if (!line) {
        perror("Failed to get GPIO line");
        gpiod_chip_close(chip);
        return 1;
    }

    ret = gpiod_line_request_output(line, "gpio_blink", 0);
    if (ret < 0) {
        perror("Failed to request line as output");
        gpiod_chip_close(chip);
        return 1;
    }

    while (1) {

        gpiod_line_set_value(line, 1);
        printf("GPIO %d HIGH\r\n", GPIO_LINE);
        sleep(SLEEP_TIME);

        gpiod_line_set_value(line, 0);
        printf("GPIO %d LOW\r\n", GPIO_LINE);
        sleep(SLEEP_TIME);

    }

    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
