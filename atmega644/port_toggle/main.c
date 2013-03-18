#include <avr/io.h>
#include <util/delay.h>


int main(void) {
	// Set PORTC:0 for output
	DDRC = 0xFF;

	while(1) {
		PORTC = 0x00; // set pin high			
	}

}
