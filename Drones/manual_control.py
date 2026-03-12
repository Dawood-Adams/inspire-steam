from pysimverse import Drone
import time
import cv2
drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
rc_speed = 250
while True:
    key = cv2.waitKey(1) & 0xff

    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0
    
    if key==ord("w"):
        forward_backward = rc_speed
    elif key==ord("s"):
        forward_backward = rc_speed
    elif key==ord("a"):
        left_right = rc_speed
    elif key==ord("d"):
        left_right = rc_speed
    elif key==ord("u"):
        up_down = rc_speed
    elif key==ord("o"):
        up_down = rc_speed
    elif key==ord("q"):
        yaw = 1
    elif key==ord("e"):
        yaw = 1
    elif key == ord("1") or key == 27:
        drone.land()
        time.sleep(2)
        break
    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )