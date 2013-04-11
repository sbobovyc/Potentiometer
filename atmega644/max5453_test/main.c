#include <util/delay.h>
#include "max5354.h"

int main(void) {

	max5354_init();

	while(1) {
		max5354_setVoltage(0.66);
		_delay_us(1);
	}
}
