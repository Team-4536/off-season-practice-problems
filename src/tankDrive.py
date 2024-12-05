from wpimath.kinematics import DifferentialDriveKinematics, ChassisSpeeds
from robotHAL import RobotHALBuffer



class tankDrive():

    def __init__(self) -> None:
        self.drivetrain = DifferentialDriveKinematics(0.8)

    def update(self, yAxis: float, xAxis: float, buf: RobotHALBuffer) -> None:
        driveSpeed = ChassisSpeeds(0, yAxis, xAxis)
        bob = self.drivetrain.toWheelSpeeds(driveSpeed)
        buf.rightDriveMotorVolts = bob.right
        buf.leftDriveMotorVolts = bob.left