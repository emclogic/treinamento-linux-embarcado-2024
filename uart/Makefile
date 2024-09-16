CC = gcc
CFLAGS = -Wall -O2
LIBS = -lserialport

all: serial_libsp

serial_libsp: serial_libsp.o
	$(CC) $(CFLAGS) -o serial_libsp serial_libsp.o $(LIBS)

serial_libsp.o: serial_libsp.c
	$(CC) $(CFLAGS) -c serial_libsp.c

clean:
	rm -f *.o serial_libsp
