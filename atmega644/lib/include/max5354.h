/**
 *	@file max5354.h
 *	@author Stanislav Bobovych
 *	@details
 *	http://datasheets.maximintegrated.com/en/ds/MAX5354-MAX5355.pdf
 */
#include <avr/io.h>

#ifndef MAX5354_H
#define MAX5354_H

#define MAX5354_VREF	1.9
#define MAX5354_GAIN	1
#define MAX5354_RANGE	1024

// commands
#define MAX5354_LD_UP	0x0000
#define MAX5354_LOAD	0x2000
#define MAX5354_UPDATE	0x4000
#define MAX5354_SHUTDN	0xE000
#define MAX5354_NOP	0x7000

// SPI stuff
#define MAX5354_DDR_CS	DDRB
#define MAX5354_PORT_CS PORTB
#define MAX5354_DD_CS 	PB4

#define MAX5354_CS_HIGH MAX5354_PORT_CS |= (1<<MAX5354_DD_CS)
#define MAX5354_CS_LOW MAX5354_PORT_CS &= ~(1<<MAX5354_DD_CS)

void max5354_init(void);
void max5354_setVoltage(float voltage);
void max5354_shutdown(void);

#endif /* MAX5354_H */
