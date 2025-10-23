from ntcore import NetworkTableInstance

from robotHAL import RobotHALBuffer
from timing import TimeData


class RobotSimHAL:
    def __init__(self):
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")
        self.buf = RobotHALBuffer()
        self.table.putNumber("motor one voltage", self.buf.motorOneVolts)
        self.table.putNumber("motor two voltage", self.buf.motorTwoVolts)

    def update(self, time: TimeData) -> None:
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")
