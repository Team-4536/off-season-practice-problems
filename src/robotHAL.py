import copy
import math

import navx
import ntcore
import rev
import wpilib
from phoenix5.led import CANdle
from phoenix6.hardware import CANcoder
from timing import TimeData


class RobotHALBuffer:
    def __init__(self) -> None:
        self.leftDriveMotorVolts = 0
        self.rightDriveMotorVolts = 0

    def resetEncoders(self) -> None:
        pass

    def stopMotors(self) -> None:
        self.leftDriveMotorVolts = 0
        self.rightDriveMotorVolts = 0

    def publish(self, table: ntcore.NetworkTable) -> None:
        table.putNumber("Left Volts", self.leftDriveMotorVolts)
        table.putNumber("Right Volts", self.rightDriveMotorVolts)


class RobotHAL:
    def __init__(self) -> None:
        self.prev = RobotHALBuffer()

        self.leftDriveMotor = rev.CANSparkMax(0, rev.CANSparkMax.MotorType.kBrushless)
        self.rightDriveMotor = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)

    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        prev = self.prev
        self.prev = copy.deepcopy(buf)

        self.leftDriveMotor.setVoltage(buf.leftDriveMotorVolts)
        self.rightDriveMotor.setVoltage(buf.rightDriveMotorVolts)
