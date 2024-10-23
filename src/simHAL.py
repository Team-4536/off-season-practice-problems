import copy
import math

from ntcore import NetworkTableInstance
from robotHAL import RobotHALBuffer
from timing import TimeData
from wpimath.geometry import Rotation2d, Translation2d


class RobotSimHAL:
    def __init__(self):
        self.prev = RobotHALBuffer()
        self.table = NetworkTableInstance.getDefault().getTable("sim")

    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        self.prev = copy.deepcopy(buf)
