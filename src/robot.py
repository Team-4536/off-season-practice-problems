import wpilib


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        pass

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
