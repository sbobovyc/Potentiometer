#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#include "uart.h"
#include "max5354.h"
#include "adc.h"

int main(void) {
	uint16_t reading = 0;
	
	USART_init();
	max5354_init();
	ADC_init();

	// set the DAC voltage to 1 V
	max5354_setVoltage(0.7);

	while(1) {
		_delay_us(1);
		// read voltage from opamp
		reading = ADC_read(ADC0D);
		// transmit over serial, little endian format
		USART_transmit((uint8_t)(reading>>8));
		USART_transmit((uint8_t)reading);
	}
}
