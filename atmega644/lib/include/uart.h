/**
 *	@file uart.h
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones uart driver hardcoded to run at 9600 baud.
 */
#ifndef UART_H
#define UART_H

void USART_init(void);
void USART_transmit(unsigned char data);

#endif /* UART_H */
