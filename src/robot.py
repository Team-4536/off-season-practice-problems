from numpy import short
from phoenix5 import ControlMode

import robotHAL
import wpilib
from ntcore import NetworkTableInstance
from simHAL import RobotSimHAL
from timing import TimeData
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import ChassisSpeeds, SwerveModulePosition, DifferentialDriveKinematics


class RobotInputs:
    def __init__(self) -> None:
        self.driveController = wpilib.XboxController(0)
        self.xDirection = 0
        self.yDirection = 0

    def update(self) -> None:
        self.xDirection = self.driveController.getRightX()
        self.yDirection = self.driveController.getLeftY()


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.time = TimeData(None)

        self.hal = robotHAL.RobotHALBuffer()

        self.hardware: robotHAL.RobotHAL | RobotSimHAL
        if self.isSimulation():
            self.hardware = RobotSimHAL()
        else:
            self.hardware = robotHAL.RobotHAL()
        self.hardware.update(self.hal, self.time)

        self.table = NetworkTableInstance.getDefault().getTable("telemetry")

        self.input = RobotInputs()

    def robotPeriodic(self) -> None:
        self.time = TimeData(self.time)

        self.hal.publish(self.table)

    def teleopInit(self) -> None:
        self.driveTrainKinamatics = DifferentialDriveKinematics(1.5)

    def teleopPeriodic(self) -> None:
        self.input.update()
        self.hal.stopMotors()

        driveTrainSpeeds = ChassisSpeeds(0, self.input.yDirection, self.input.xDirection)
        driveTrainWheelSpeeds = self.driveTrainKinamatics.toWheelSpeeds(driveTrainSpeeds)

        self.hal.leftDriveMotorVolts = driveTrainWheelSpeeds.left
        self.hal.rightDriveMotorVolts = driveTrainWheelSpeeds.right

        self.hardware.update(self.hal, self.time)

    def disabledPeriodic(self) -> None:
        self.hal.stopMotors()
        self.hardware.update(self.hal, self.time)
