import wpilib
from ntcore import NetworkTableInstance


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.table = NetworkTableInstance.getDefault().getTable("telementry")
        self.table.putNumber("voltage", 1)

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        voltage = 5
        self.table.putNumber("voltage", voltage)

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
