#include <util/delay.h>
#include "uart.h"


int main(void) {

	USART_Init();

	while(1) {
		_delay_ms(20.0);
		USART_Transmit(0x41);
		USART_Transmit(0x0D);
		USART_Transmit(0x0A);
		//USART_Transmit("\r");
		//USART_Transmit("\n");
	}
}
