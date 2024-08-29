CC=gcc
CFLAGS=-Wall -g
LIBS=-lgpiod

all: gpio_blink

gpio_blink: gpio_blink.c
	$(CC) $(CFLAGS) gpio_blink.c -o gpio_blink $(LIBS)

clean:
	rm -f gpio_blink
