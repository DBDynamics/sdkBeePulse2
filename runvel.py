import time

from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
mid = 0
m.setVelocityMode(mid)
m.setTargetVelocity(mid, 1000)

# m.setPowerOn(mid)

m.stop()