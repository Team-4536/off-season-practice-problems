import wpilib
import rev
from rev import SparkMax


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.Motor = SparkMax(2, SparkMax.MotorType.kBrushless)

        self.motorCtrlr = wpilib.XboxController(0)

        self.Motor.set(0)

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self):

        aDown = self.motorCtrlr.getAButton()


if __name__ == "__main__":
    wpilib.run(Robot)
