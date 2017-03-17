import spidev
import time


bus = 0
device = 0
spi = spidev.SpiDev(bus, device)
spi.open(0, 0)


spi.mode = 0b11
spi.max_speed_hz = 50
spi.cshigh = False

spi_send = [0xff, 0xa4]
duan_code = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90]
wei_code = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]


def display(num):
    bit0 = num % 10
    bit1 = num / 10 % 10
    bit2 = num / 100 % 10
    bit3 = num / 1000 % 10

try:
    while True:
        resp = spi.xfer(spi_send)
except KeyboardInterrupt:
    print("exit")
    spi.close()