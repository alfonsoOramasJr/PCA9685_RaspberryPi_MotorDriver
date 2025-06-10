# MotorDriver.py
The motor driver python script is just another abstract layer on top of the Adafruit_PCA9685 library.

Import the driver as follows,

```python
from MotorDriver import MotorDriver
```

which will then give you access to give the motor a specific PWM signal to a specific Channel, you can also <strong>set up the frequency for the motor driver </strong> if you have to by including it as an argument when you create the object of the ```MotorDriver``` class.

```python
from MotorDriver import MotorDriver
motor_driver = MotorDriver(50) ## 50 Hertz
motor_driver.set_throttle(20, 0) ## 20%, 1st Channel
```

If you're just copying the code, remember to change the library name 'MotorDriver' to whatever you want as follows,
```python
from MySeparateFile import MotorDriver
```