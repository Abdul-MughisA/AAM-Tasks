import math
import time

speed = 0

for i in range(-90, 90):
    speed = math.sin(math.radians(i))*4
    print(speed)
    time.sleep(0.2)
#end for