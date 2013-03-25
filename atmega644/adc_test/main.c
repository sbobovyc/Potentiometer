#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#include "adc.h"


int main(void) {
	uint16_t reading = 0;

	ADC_init();

	while(1) {
		_delay_us(1);
		reading = ADC_read(ADC0D);
	}
}
