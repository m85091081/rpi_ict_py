import serial

ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
        )

ser.open()
ser.write(serial.to_bytes([0x30]))
sleep(1)
ser.readline()
ser.write(serial.to_bytes([0x02]))
