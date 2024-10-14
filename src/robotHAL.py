import copy
import math

import navx
import ntcore
import rev
import wpilib
from phoenix5.led import CANdle
from phoenix6.hardware import CANcoder
from timing import TimeData


# The HAL buffer contains all input and output variables which
# connect the robot general code (robot.py) to the robot 
# hardware (RobotHAL below). Put all variables in this class 
# like motor voltages and motor speeds.
class RobotHALBuffer():
    # Initialize all variables to a safe value (usually stopped)
    def __init__(self) -> None:
        self.shooterSpeed: float = 0 # -1 to 1 volts to motor controller
        pass

    # Set all variables to a shutdown "safe" value. Usually this
    # is just stopped, but it could be more complicated (like
    # hold position for an elevator you don't want to drop to the
    # ground.)
    def stopMotors(self) -> None:
        self.shooterSpeed = 0 # -1 to 1 volts to motor controller
        pass

    # Send robot HALBuffer values to the driver station computer
    def publish(self, table: ntcore.NetworkTable) -> None:
        table.putNumber("ShooterSpeed", self.shooterSpeed)
        pass

# The RobotHAL sends the values in the HALBuffer to the motors
class RobotHAL():
    # Define motor objects in RobotHAL:init
    def __init__(self) -> None:
        self.prev = RobotHALBuffer()

        self.shooterMotor = rev.CANSparkMax(11, rev.CANSparkMax.MotorType.kBrushless)

    # Send values in the RobotHALBuffer to the motors and update values
    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        prev = self.prev
        self.prev = copy.deepcopy(buf)

        self.shooterMotor.set(buf.shooterSpeed)

