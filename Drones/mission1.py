from pysimverse import Drone
import time
drone = Drone()
drone.connect()

drone.take_off(5)
# distance in cm
drone.set_speed(1000)
drone.move_forward(250)

drone.move_right(220)

drone.land()
