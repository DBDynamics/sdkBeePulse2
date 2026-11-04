import time

from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
mid = 1
m.setTargetPosition(mid, 100)
for loop in range(0, 100):
    print("link status:", m.getLinkStatus())
    time.sleep(0.1)

# m.setPowerOn(mid)
time.sleep(1)
m.stop()
