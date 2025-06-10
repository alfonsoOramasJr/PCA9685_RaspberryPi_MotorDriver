import time
from MotorDriver import MotorDriver
motor_driver = MotorDriver(50)

first_pwm_channel = 0
arming_time_in_seconds = 2

## Motor arming sequence.
motor_driver.set_throttle(0, first_pwm_channel)
time.sleep(arming_time_in_seconds)

## Basic motor test after arming.
motor_driver.set_throttle(10, first_pwm_channel)
time.sleep(1)
motor_driver.set_throttle(0, first_pwm_channel)