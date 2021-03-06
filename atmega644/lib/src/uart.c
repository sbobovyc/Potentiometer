/**
 *	@file uart.c
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones uart driver hardcoded to run at 9600 baud.
 */
#include <avr/io.h>

#include "uart.h"

void USART_init(void)
{
	#define BAUD 9600
	#include <util/setbaud.h>
	/* Set baud rate*/
	UBRR0H = UBRRH_VALUE; 
	UBRR0L = UBRRL_VALUE;
	/* Enable receiver and transmitter*/
	UCSR0B = (1<<RXEN0)|(1<<TXEN0);
	/* Set frame format: 8data, 1 stop bit*/
	UCSR0C = (0<<USBS0)|(3<<UCSZ00);
}

void USART_transmit(unsigned char data)
{
	/* Wait for empty transmit buffer*/
	while( !( UCSR0A & (1<<UDRE0)) );
	/* Put data into buffer, sends the data*/
	UDR0 = data;
}

