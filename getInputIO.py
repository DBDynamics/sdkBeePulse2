import time

from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
mid = 1

for loop in range(0, 100):
    time.sleep(0.5)
    sensor = m.getInputIO(mid)
    if sensor&0x1:
        print("input 0")

    if sensor & 0x2:
        print("input 1")

    if sensor & 0x4:
        print("input 2")

# m.setPowerOn(mid)

m.stop()