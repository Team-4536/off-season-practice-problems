import rev
import wpilib
from ntcore import NetworkTableInstance


class RobotHALBuffer:
    def __init__(self):
        self.motorOneVolts = 0
        self.motorTwoVolts = 0
        self.controller = wpilib.XboxController(0)
        self.aButton = self.controller.getAButton()
        self.bButton = self.controller.getBButton()
        self.xButton = self.controller.getXButton()
        self.yButton = self.controller.getYButton()


class RobotHAL:
    def __init__(self):
        self.motorOne = rev.SparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.motorTwo = rev.SparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")

    def update(self, buf: RobotHALBuffer):
        self.motorOne.set(buf.motorOneVolts)
        self.motorTwo.set(buf.motorTwoVolts)
