#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#include "spi.h"

#define DDR_CS	DDRB
#define PORT_CS PORTB
#define DD_CS 	PB4

#define CS_HIGH PORT_CS |= (1<<PB4)
#define CS_LOW PORT_CS &= ~(1<<PB4)

int main(void) {
	uint16_t command = 0x1FF8; // Dac reg = 1023, Vout = 0.75 V
	//uint16_t command = 0x0008; // DAC reg = 1, Vout = 0.0013 V
	DDR_CS |= (1<<DD_CS); // SPI CS, output

	SPI_Init();

	while(1) {
		CS_LOW;
		_delay_us(1);
		SPI_Send(command>>8);
		SPI_Send(command);
		CS_HIGH;
		_delay_us(1);
	}
}
