import wpilib
import rev
from rev import SparkMax
from ntcore import NetworkTableInstance


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:

        self.MAX_VOLTAGE = 2  # Max speed
        self.Motor = SparkMax(2, rev.SparkMax.MotorType.kBrushless)

        self.Motor.set(0)

        self.table = NetworkTableInstance.getDefault().getTable("telementry")

        self.driveCtrlr = wpilib.XboxController(0)

        self.joyY = self.driveCtrlr.getLeftY()

        self.voltage = self.Motor.getBusVoltage() * self.Motor.getAppliedOutput()

        self.table.putNumber("Motor Voltage", self.voltage)
        self.table.putNumber("Left Joystick Y", self.joyY)

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self):

        self.voltage = self.Motor.getBusVoltage() * self.Motor.getAppliedOutput()
        self.table.putNumber("Motor Voltage", self.voltage)
        self.joyY = self.driveCtrlr.getLeftY()
        self.table.putNumber("Left Joystick Y", self.joyY)
        setPoint = 0

        if self.joyY < -0.08:
            setPoint = self.joyY * self.MAX_VOLTAGE

        self.Motor.setVoltage(setPoint)


if __name__ == "__main__":
    wpilib.run(Robot)
