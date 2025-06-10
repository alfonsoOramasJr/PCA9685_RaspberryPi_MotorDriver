"""
MotorDriver.py

This file functions as a API for sending PWM signals through the
PCA9685 16 Channel Driver I2C Module to an electronic speed controller.

    * Example use case in a DIFFERENT file is as follows:
            from MotorDriver import MotorDriver
            
            motor_driver = MotorDriver(50)
            motor_driver.set_throttle(20, 0)

    * The motor driver code above sent out a 20% throttle signal to the 1st channel of the
    PCA9685 16 Channel Driver I2C Module.

    * Channel Numbers are 0-indexed, the 16th channel from the pwm board would have a value
    of 15, (0-15).

    * The frequency for the PWM signal is also initialized in the beginning of the program,
    which can be set to any integer value. The current default value is 50 Hz.

"""

import sys
try:
    from Adafruit_PCA9685 import PCA9685
except ImportError:
    print(
        "Error: The Adafruit_PCA9685 library is not installed.\n"
        "Install it using: 'pip install Adafruit-PCA9685'"
    )
    sys.exit(1)

class MotorDriver:
    def __init__(self, pwm_frequency=50): ## 50 Hz default value.
        self.ESC_MIN = 205
        self.ESC_MAX = 410

        self.pwm_driver = PCA9685()
        self.pwm_driver.set_pwm_freq(pwm_frequency)

    def set_pwm_value_to_channel(self, pwm_value, channel_number):
        self.pwm_driver.set_pwm(channel_number, 0, int(pwm_value))
    
    def get_safe_percent(self, percent_input):
        return max(0, min(100, percent_input))

    def set_throttle(self, percent_input, channel_number):
        percent = self.get_safe_percent(percent_input)
        pwm_value = self.ESC_MIN + ((self.ESC_MAX - self.ESC_MIN) * (percent / 100.0))
        self.set_pwm_value_to_channel(pwm_value, channel_number)