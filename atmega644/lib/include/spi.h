/**
 *	@file spi.h
 *	@author Stanislav Bobovych
 *	@details
 *	Bare bones master spi driver.
 */
#ifndef SPI_H
#define SPI_H

#define DDR_SPI DDRB
#define DD_MOSI PB5
#define DD_MISO	PB6
#define DD_SCK	PB7

void SPI_init(void);
void SPI_send(char cData);
char SPI_receive(void);
#endif /* SPI_H */

