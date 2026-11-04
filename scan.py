from DBDynamics import Bee
# for windows, m = Bee('com3')
m = Bee('/dev/ttyUSB0')

a = m.scanDevices()
print(a)

m.stop()
