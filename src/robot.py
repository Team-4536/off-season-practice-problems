import wpilib
from ntcore import NetworkTableInstance
import rev
from rev import SparkMax


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:

        self.driveCtrlr = wpilib.XboxController(0)

        self.Motor = SparkMax(2, rev.SparkMax.MotorType.kBrushless)

        self.Motor.set(0)
        self.table = NetworkTableInstance.getDefault().getTable("telementry")
        self.table.putNumber("voltage", 1)

    def robotPeriodic(self) -> None:
        self.table.putNumber(  # This doesn't work in sim! Yet...
            "motorOutput",
            self.Motor.getAppliedOutput(),
        )

    def teleopInit(self) -> None:
        self.on = False

        voltage = 5
        self.table.putNumber("voltage", voltage)

    def teleopPeriodic(self):
        pressedA = self.driveCtrlr.getAButtonPressed()

        if pressedA:
            self.on = not self.on

        if self.on:
            self.Motor.set(0.2)
        else:
            self.Motor.set(0)


if __name__ == "__main__":
    wpilib.run(Robot)
