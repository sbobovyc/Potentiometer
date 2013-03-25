#include <util/delay.h>
#include "uart.h"


int main(void) {

	USART_init();

	while(1) {
		_delay_ms(20.0);
		USART_transmit(0x41);
		USART_transmit(0x0D);
		USART_transmit(0x0A);
		//USART_transmit("\r");
		//USART_transmit("\n");
	}
}
