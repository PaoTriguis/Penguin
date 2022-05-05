import rodi
import time

robot = rodi.RoDI()

robot.sing(33, 1000)
time.sleep(1)
   
print("RoDI do a rainbow")
for j in range(256):
    red, green, blue = wheel(j)
    robot.pixel(red, green, blue)
    time.sleep(0.005)
    robot.pixel(0, 0, 0)