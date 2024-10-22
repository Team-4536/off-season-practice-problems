import copy
import math

from ntcore import NetworkTableInstance
from robotHAL import RobotHALBuffer
from timing import TimeData
from wpimath.geometry import Rotation2d, Translation2d

def lerp(a: float, b: float, t: float) -> float:
    return a + (b-a)*t

# spoofs values of the actual motors to allow for testing
class RobotSimHAL():
    def __init__(self):
        self.prev = RobotHALBuffer()
        self.table = NetworkTableInstance.getDefault().getTable("sim")

        self.leftMotorVelocity = 0
        self.rightMotorVelocity = 0

    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        self.prev = copy.deepcopy(buf)

        self.leftMotorVelocity = lerp(self.leftMotorVelocity, buf.leftTankVolts * 1/0.2, 0.2)
        self.rightMotorVelocity = lerp(self.rightMotorVelocity, buf.rightTankVolts * 1/0.2, 0.2)

        buf.leftTankMorotEncoderValue += self.leftMotorVelocity * time.dt
        buf.rightTankMorotEncoderValue += self.rightMotorVelocity * time.dt
