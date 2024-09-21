
# AVR UART Communication with Live Data Transmission Speed

This project demonstrates a full-duplex UART communication system between an AVR microcontroller ATmega328p (Arduino) and a PC. The Arduino receives data via UART, stores it in EEPROM, and sends it back to the PC. The PC script prints live data transmission speed during both sending and receiving processes.

## Table of Contents

- [Overview](#overview)
- [Setup and Requirements](#setup-and-requirements)
- [Usage](#usage)
  - [Flashing the MCU](#flashing-the-mcu)
  - [Running the Python Script](#running-the-python-script)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project consists of two parts:

1. **Embedded C Project (Atmel Studio)**: The Arduino uses UART to communicate with the PC, storing incoming data in EEPROM and sending it back after the full transmission. (or) An INO file built using avr library for UART capabilities that can be run on Arduino IDE.
2. **Python Script**: A serial communicator that sends data to the MCU, receives the stored data back, and tracks the real-time data transmission speed without relying solely on the baud rate.

### Features

- Bi-directional UART communication between the Arduino and the PC.
- Real-time calculation and display of data transmission speed in bits per second.
- Data is stored in the MCU EEPROM and retrieved after full transmission.


## Setup and Requirements

### Hardware

- **MCU**: ATmega328p (or compatible Arduino board).
- **PC**: A computer with a USB-to-serial adapter to communicate with the MCU.

### Software

- [Atmel Studio](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio) or [Arduino IDE](https://www.arduino.cc/en/software) to compile and flash the MCU code.
- [AVRDUDE](http://www.nongnu.org/avrdude/) for flashing the compiled hex file onto the microcontroller.
- Python 3.x installed on your PC, with the `pyserial` module:
  
  Install `pyserial` via pip:
  ```bash
  pip install pyserial
  ```


  ## Usage

### Flashing the MCU

1.  **Compile the Atmel Studio Project**: Open the Atmel Studio project located at:
    
  ```bash
  assignment_nymble_atmel_studio/assignment_nymble.atsln
  ```
  
2.  **Flash the MCU** using AVRDUDE:
Use the following command to flash the hex file to your ATmega328p (or) Upload using Arduino IDE:
  ```bash
avrdude -v -V -patmega328p -carduino "-PCOM4" -b115200 -D "-Uflash:w:assignment_nymble_atmel_studio\assignment_nymble\Debug\assignment_nymble.hex:i"
```
-   Replace `COM4` with the correct COM port for your setup.
-   Ensure that the baud rate and paths to the hex file are correct.



### Running the Python Script
Execute the Python script for communication with the MCU:
```bash
python ./nymble_assignment_python/serial_communicator.py
```
**Live Transmission Speed**: The script will send data to the MCU and display real-time transmission speed (in bits per second) while sending and receiving data.

**Example Output**
When the script is running, it will display output similar to the following:

```yaml
Starting data transmission...
Total bytes sent: 1000
Sending speed: 2026.67 bits/sec
Live receiving speed: 1582.38 bits/sec
Live receiving speed: 2096.50 bits/sec
Live receiving speed: 2121.35 bits/sec
Live receiving speed: 2048.78 bits/sec
Received: Text from EEPROM... 

Termination character received. Exiting...
```
    
