#include <avr/io.h>
#include <util/delay.h>

#include "spi.h"

#define DDR_CS	DDRB
#define PORT_CS PORTB
#define DD_CS 	PB4

#define CS_HIGH PORT_CS |= (1<<PB4)
#define CS_LOW PORT_CS &= ~(1<<PB4)

int main(void) {
	DDR_CS |= (1<<DD_CS); // SPI CS, output

	SPI_Init();

	while(1) {
		CS_HIGH;
		SPI_Send(0xAA);
		CS_LOW;
	}

}
