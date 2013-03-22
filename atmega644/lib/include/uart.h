/**
 *	@file uart.h
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones uart driver hardcoded to run at 9600 baud.
 */
#ifndef UART_H
#define UART_H

void USART_Init(void);
void USART_Transmit(unsigned char data);

#endif /* UART_H */
