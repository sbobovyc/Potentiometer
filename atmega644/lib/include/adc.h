/**
 *	@file adc.c
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones adc driver.
 *	http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=56429
 */

#ifndef ADC_H
#define ADC_H

#include <avr/io.h>

void ADC_Init(void);

/*
 * @param channel is any single ended adc channel, ADC0D through ADC7D
 */
uint16_t ADC_Read(uint8_t channel); 

#endif /* ADC_H */
