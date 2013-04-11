/**
 *	@file max5354.c
 *	@author Stanislav Bobovych
 *	@details
 *	http://datasheets.maximintegrated.com/en/ds/MAX5354-MAX5355.pdf
 */
#include <stdint.h>
#include <util/delay.h>
#include "spi.h"
#include "max5354.h"

#define DDR_CS	DDRB
#define PORT_CS PORTB
#define DD_CS 	PB4

#define CS_HIGH PORT_CS |= (1<<PB4)
#define CS_LOW PORT_CS &= ~(1<<PB4)

void max5354_init(void) {
	// set SPI CS as output
	MAX5354_DDR_CS |= (1<<MAX5354_DD_CS); // SPI CS, output
	SPI_init();
}

void max5354_setVoltage(float voltage) {
	uint16_t command = 0;
	uint16_t NB = 0;

	// calculate DAC value, clamp if overflows
	NB = (uint16_t)(voltage*MAX5354_RANGE/MAX5354_GAIN)/MAX5354_VREF;
	if(NB > 1023)
		NB = 1023;

	// load and update DAC
	command = MAX5354_LD_UP | (NB<<3);
	MAX5354_CS_LOW;
	_delay_us(1);
	// uint16_t is little endian on avr, DAC expects first byte to have MSB
	SPI_send((uint8_t)(command>>8));	// byte with MSB
	SPI_send((uint8_t)(command));	// lower byte
	MAX5354_CS_HIGH;
	_delay_us(1);
}

void max5354_shutdown(void) {
	MAX5354_CS_LOW;
	_delay_us(1);
	SPI_send(MAX5354_SHUTDN>>8);
	SPI_send(0);
	MAX5354_CS_HIGH;
}
