from pysimverse import Drone
import time
drone = Drone()
drone.connect()

drone.take_off(100)
# distance in cm

drone.move_forward(80)
time.sleep(1)
drone.move_backward(80)
time.sleep(2)

drone.move_right(30)
time.sleep(2)
drone.move_left(30)

drone.land()
