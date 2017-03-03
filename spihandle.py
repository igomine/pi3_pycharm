import time
import spidev

bus = 0
device = 0
spi = spidev.SpiDev(bus, device)
spi.open(0, 0)

spi.mode = 0b11
spi.max_speed_hz = 1000000
spi.cshigh = False