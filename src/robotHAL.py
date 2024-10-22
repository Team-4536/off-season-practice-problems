import copy
import math

import navx
import ntcore
import rev
import wpilib
from phoenix5.led import CANdle
from phoenix6.hardware import CANcoder
from timing import TimeData


class RobotHALBuffer():
    # runs once when the RobotHALBuffer is made
    # put all variables wanted in this class here, like motor voltages and motor speeds
    def __init__(self) -> None:
        self.gyroAngle: float = 0
        self.leftTankVolts: float = 0
        self.rightTankVolts: float = 0

        self.leftTankVelocity: float = 0
        self.rightTankVelocity: float = 0
        
        self.leftTankMorotEncoderValue = 0
        self.rightTankMorotEncoderValue = 0

    # make all encoders become 0
    def resetEncoders(self) -> None:
        pass

    # make all motors stop
    def stopMotors(self) -> None:
        self.leftTankVolts: float = 0
        self.rightTankVolts: float = 0

    # publish the data read from motors, like encoder values
    def publish(self, table: ntcore.NetworkTable) -> None:
        table.putNumber("Left wheel tank volts", self.leftTankVolts)
        table.putNumber("Right wheel tank volts", self.rightTankVolts)

# this class actually sends the values in the HALBuffer to the motors
class RobotHAL():
    # define motors here
    def __init__(self) -> None:
        self.prev = RobotHALBuffer()

        self.gyro  = navx.AHRS(wpilib.SerialPort.Port.kUSB1)

        self.leftTankMotor = rev.CANSparkMax(0, rev.CANSparkMax.MotorType.kBrushless)
        self.rightTankMotor = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)

        self.leftTankMotorEncoder = self.leftTankMotor.getEncoder()
        self.rightTankMotorEncoder = self.rightTankMotor.getEncoder()

    # send values found in the Hal Buffer to the motors and update values found in the hal buffer like encoder positions
    def update(self, buf: RobotHALBuffer, time: TimeData) -> None:
        prev = self.prev
        self.prev = copy.deepcopy(buf)

        buf.gyroAngle = self.gyro.getAngle()

        self.leftTankMotor.setVoltage(buf.leftTankVolts)
        self.rightTankMotor.setVoltage(buf.rightTankVolts)

        buf.leftTankMorotEncoderValue = self.leftTankMotorEncoder.getPosition()
        buf.rightTankMorotEncoderValue = self.rightTankMotorEncoder.getPosition()