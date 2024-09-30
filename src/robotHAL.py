import copy
import math

import navx
import ntcore
import rev
import wpilib
from phoenix5.led import CANdle
from phoenix6.hardware import CANcoder
from timing import TimeData


class RobotHALBuffer():
    # runs once when the RobotHALBuffer is made
    # put all variables wanted in this class here, like motor voltages and motor speeds
    def __init__(self) -> None:
        pass

    # make all encoders become 0
    def resetEncoders(self) -> None:
        pass

    # make all motors stop
    def stopMotors(self) -> None:
        pass

    # publish the data read from motors, like encoder values
    def publish(self, table: ntcore.NetworkTable) -> None:
        pass

# this class actually sends the values in the HALBuffer to the motors
class RobotHAL():
    # define motors here
    def __init__(self) -> None:
        self.prev = RobotHALBuffer()

    # send values found in the Hal Buffer to the motors and update values found in the hal buffer like encoder positions
    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        prev = self.prev
        self.prev = copy.deepcopy(buf)