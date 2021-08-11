# ESP32_sds011_MicroPython
pm2.5 sensor driver for ESP32

## Introduction
Both sds011.py and sds011_simpletest.py come from [here](https://github.com/alexmrqt/micropython-sds011), where I made some changes to make this code works for my ESP32.

### changes I made
- when calling make_command, all parameter shall be bytes.
- before reading the sensor status, give sensor 30s work.
- after query, wait 3s so the reading won't be failed easily.
- change the way to calculate checksum.

## UART

```python
uart = UART(1,baudrate=9600, bits=8, parity=None, stop=1, rx=14,tx=12)
```

For ESP32, when you connect it through USB, you can't use UART0, it's used for REPL, you can only use UART1 or UART2, then you have to indicate pins you choose, 
in here I use pin12 for tx, pin14 for rx. 

## connection

My ESP32 board has 5V output directly comes from the USB interface, that's where I get the 5V sds011 needs, then connect the ground, 
connect tx of ESP32 to rx of sds011, rx of ESP32 to rx of sds011.

# note

This driver will change ESP32 mode to query, if later you remove it from ESP32 and install it throught USB interface of raspberry pi, you need to reconfigure 
the sds011 to active mode to make the code work in most situation, if like me, you are using 
[this library from pypi](https://github.com/menschel/sds011/blob/master/sds011/sds011.py) then you will need to  add this line of code
```python
set_data_reporting(mode_select="active")
```
