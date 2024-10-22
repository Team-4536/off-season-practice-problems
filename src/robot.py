from numpy import short
from phoenix5 import ControlMode
import wpilib.shuffleboard

import robotHAL
import wpilib
from ntcore import NetworkTableInstance
from simHAL import RobotSimHAL
from timing import TimeData
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import ChassisSpeeds, SwerveModulePosition

from tankDrive import TankDrivetrain


class RobotInputs():
    def __init__(self) -> None:
        # make a controller object and inputs you will grab from controller
        self.driveCtrlr = wpilib.Joystick(0) #wpilib.XboxController(0)
        self.driveX = 0
        self.driveY = 0

    def update(self) -> None:
        # update the inputs defined in the __init__ method
        self.driveX = self.driveCtrlr.getRawAxis(wpilib.Joystick.AxisType.kXAxis)
        self.driveY = self.driveCtrlr.getRawAxis(wpilib.Joystick.AxisType.kYAxis)

class Robot(wpilib.TimedRobot):
    # this method runs once when the robot is turned on
    def robotInit(self) -> None:
        self.time = TimeData(None)

        # hal buffer is where motor data will be sent to and recieved from
        self.hal = robotHAL.RobotHALBuffer()

        # determining if the robot is actually running or in a simulation
        self.hardware: robotHAL.RobotHAL | RobotSimHAL
        if self.isSimulation():
            self.hardware = RobotSimHAL()
        else:
            self.hardware = robotHAL.RobotHAL()
        self.hardware.update(self.hal, self.time)

        # makes a telemetry table that data can be sent to
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")

        self.odomField = wpilib.Field2d()
        wpilib.SmartDashboard.putData("odom", self.odomField)


        # making an instance of the robotInputs class defined earlier
        self.input = RobotInputs()

    # this method runs continuously whenever the robot is on
    def robotPeriodic(self) -> None:
        # updating time
        self.time = TimeData(self.time)

        # updating the telemetry table


    # this method runs once when teleop Mode is enabled
    def teleopInit(self) -> None:
        self.drivetrain = TankDrivetrain(self.hal)

    # this method runs continously after teleop Mode is enabled
    def teleopPeriodic(self) -> None:
        # update the RobotInputs object defined in robotInit to pull values from the controllers
        self.input.update()
        # turn all motors off
        self.hal.stopMotors()

        self.drivetrain.update(self.input.driveX, self.input.driveY, self.hal)

        position: Pose2d = self.drivetrain.odom.getPose()
        self.odomField.setRobotPose(position)

        self.hal.publish(self.table)

        # update the hal with the hal buffer and current time
        self.hardware.update(self.hal, self.time)

    # this method runs condinously after the robot is disabled
    def disabledPeriodic(self) -> None:
        self.hal.stopMotors()
        self.hardware.update(self.hal, self.time)

# actually starts the robot
if __name__ == "__main__":
    wpilib.run(Robot)