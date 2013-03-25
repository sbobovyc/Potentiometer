/**
 *	@file adc.c
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones adc driver.
 *	http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=56429
 */
#include <avr/io.h>

#include "adc.h"

void ADC_init(void) {	
	// 16 mhz clock, we need ADC input frequency between 50 khz and 200 khz
	// 16 mhz / 128 = 125 khz
	ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); 

	// use AVCC as refrence
	ADMUX |= (1 << REFS0); 
}

uint16_t ADC_read(uint8_t channel) {
	uint16_t result = 0;
	// select channel
	ADMUX |= channel;	

	// enable adc
	ADCSRA |= (1<<ADEN); 

	// wait for conversion to finish 
	while(ADCSRA & (1<<ADSC));

	result = ADCH<<8;
	result = result | ADCL;

	return result;
}	

