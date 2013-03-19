#include <avr/io.h>
#include <util/delay.h>


int main(void) {
	// Set PORTC:0 for output
	DDRC = 0xFF;

	while(1) {
		_delay_ms(20.0);
		PORTC = (1<<PC0); // set pin high			
		_delay_ms(20.0);
		PORTC = (0<<PC0); // set pin low
	}

}
