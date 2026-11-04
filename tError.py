import random
import time

from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
mid = 31
m.setAccTime(mid, 450)
m.setTargetVelocity(mid, 100)
k = 51200 / 48.0
for loop in range(0, 10):
    m.setTargetVelocity(mid, 100)
    if m.checkSafety(31, 100):
        print("online")
    else:
        print("offline")
    time.sleep(5)
    # if m._error_axis_num > -1:
    #     print("error ", m._error_axis_num)
    # else:
    #     m.setTargetPosition(mid, 0 * k)
    # # m.waitTargetPositionReached(mid)
    # time.sleep(5)
    # if m._error_axis_num > -1:
    #     print("error ", m._error_axis_num)
    # else:
    #     m.setTargetPosition(mid, 30000)
    # time.sleep(5)
    # m.waitTargetPositionReached(mid)

m.stop()
