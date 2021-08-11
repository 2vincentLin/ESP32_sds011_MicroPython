from machine import UART, Pin
import time
import sds011

# uart = UART(1, baudrate=9600, pins=('P1','P3'))
# uart = UART(1, baudrate=9600)
# uart = UART(1, baudrate=9600, tx=1, rx=3, timeout=10)
uart = UART(1,baudrate=9600, bits=8, parity=None, stop=1, rx=14,tx=12)
dust_sensor = sds011.SDS011(uart)
dust_sensor.sleep()
dust_sensor.wake()

while True:
    
    
    dust_sensor.wake()
    time.sleep(30)

    #Returns NOK if no measurement found in reasonable time
  
    status = dust_sensor.read()
    #Returns NOK if checksum failed
    pkt_status = dust_sensor.packet_status

    if(status == False):
        print('Measurement failed.')
    elif(pkt_status == False):
        print('Received corrupted data.')
    else:
        print('PM25: ', dust_sensor.pm25)
        print('PM10: ', dust_sensor.pm10)

    #Stop fan 
    #dust_sensor.sleep()
