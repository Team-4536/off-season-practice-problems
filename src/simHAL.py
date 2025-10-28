from ntcore import NetworkTableInstance
from timing import TimeData


class RobotSimHAL:
    def __init__(self):
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")
        self.table.putBoolean("A", False)
        self.table.putBoolean("B", False)
        self.table.putBoolean("Y", False)
        self.table.putBoolean("X", False)

    def update(self) -> None:
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")
