#include <util/delay.h>
#include "max5354.h"

int main(void) {

	max5354_init();

	while(1) {
		max5354_setVoltage(1.5);
		_delay_us(1);
	}
}
