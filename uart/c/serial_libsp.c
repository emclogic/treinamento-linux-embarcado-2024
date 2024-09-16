#include <stdio.h>
#include <libserialport.h>

int main() {
    struct sp_port *port;
    const char *port_name = "/dev/ttyAMA0";

    if (sp_get_port_by_name(port_name, &port) != SP_OK) {
        printf("Error finding port %s\n", port_name);
        return -1;
    }

    if (sp_open(port, SP_MODE_READ_WRITE) != SP_OK) {
        printf("Error opening port %s\n", port_name);
        return -1;
    }

    sp_set_baudrate(port, 115200);
    sp_set_bits(port, 8);
    sp_set_parity(port, SP_PARITY_NONE);
    sp_set_stopbits(port, 1);
    sp_set_flowcontrol(port, SP_FLOWCONTROL_NONE);

    const char *msg = "Hello World, Serial in C!\n";
    int bytes_written = sp_nonblocking_write(port, msg, strlen(msg));
    if (bytes_written < 0) {
        printf("Error writing to serial port\n");
    } else {
        printf("Successfully written %d bytes to %s\n", bytes_written, port_name);
    }

    sp_close(port);
    sp_free_port(port);

    return 0;
}
