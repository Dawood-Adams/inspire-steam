from pysimverse import Drone
import time
drone = Drone()
drone.connect()

drone.take_off()

left_right = 0
forward_backward = 10
up_down = 0
yaw = 0

while True:
    drone.send_rc_control(
        left_right=left_right,
        forward_backward=forward_backward,
        up_down=up_down,
        yaw=yaw
    )