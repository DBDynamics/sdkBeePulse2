import time
from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
mid = 1
m.setTargetPosition(id=mid, value=100)
ret = m.checkSafety(100)
if ret == 1:
    print("yes")
else:
    print("no")
m.setOutputIO(mid, 0x1 << 1)

m.checkSafety(100)
if ret == 1:
    print("yes")
else:
    print("no")
time.sleep(1)
m.stop()
