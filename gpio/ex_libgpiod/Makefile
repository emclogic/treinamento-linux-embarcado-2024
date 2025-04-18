CC=aarch64-none-linux-gnu-gcc
CFLAGS=-Wall -g
LIB_NAME=gpiod
LIB_PATH=./libgpiod-1.6.3/rootfs/lib
INC=./libgpiod-1.6.3/rootfs/include

all: gpio_blink

gpio_blink: gpio_blink.c
	$(CC) $(CFLAGS) gpio_blink.c -o gpio_blink -L$(LIB_PATH) -I$(INC) -l$(LIB_NAME)

clean:
	rm -f *~ gpio_blink gpio_blinks
