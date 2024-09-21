#include <avr/io.h>
#include <avr/eeprom.h>
#include <util/delay.h>

#define F_CPU 16000000UL
#define BAUD 2400
#define MYUBRR F_CPU/16/BAUD-1

void uart_init(unsigned int ubrr) {
	UBRR0H = (unsigned char)(ubrr >> 8);
	UBRR0L = (unsigned char)ubrr;

	UCSR0B = (1 << RXEN0) | (1 << TXEN0);
	UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void uart_transmit(unsigned char data){
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

unsigned char uart_receive(void) {
	while (!(UCSR0A & (1 << RXC0)));
	return UDR0;
}


void store_data_in_eeprom(uint16_t addr, uint8_t data) {
	eeprom_write_byte((uint8_t*)addr, data);
}

uint8_t read_data_from_eeprom(uint16_t addr) {
	return eeprom_read_byte((uint8_t*)addr);
}

int main(void) {
	uart_init(MYUBRR);

	while(1){
		
		uint16_t eeprom_addr = 0;
		char data;
		while(1){
			data = uart_receive();
			
			store_data_in_eeprom(eeprom_addr++, data);
			if(data == '\n'){
				break;
			}
		}

		eeprom_addr = 0;
		while(1){
			data = read_data_from_eeprom(eeprom_addr++);
			uart_transmit(data);
			if(data == '\n'){
				break;
			}
		}

	}
	
	return 0;
}
