from wpimath.kinematics import DifferentialDriveKinematics, ChassisSpeeds, DifferentialDriveWheelSpeeds, DifferentialDriveOdometry
from wpimath.geometry import Rotation2d
from math import atan2, radians
from robotHAL import RobotHALBuffer


class TankDrivetrain():
    def __init__(self, hal: RobotHALBuffer):
        self.drivetrain = DifferentialDriveKinematics(2)
        self.odom = DifferentialDriveOdometry(Rotation2d(radians(hal.gyroAngle)), hal.leftTankMorotEncoderValue, hal.rightTankMorotEncoderValue)
    
    def update(self, xAxis, yAxis, hal: RobotHALBuffer) -> None:
        angle = atan2(yAxis, xAxis)
        speed: ChassisSpeeds = ChassisSpeeds(xAxis, yAxis, angle)
        
        wheelSpeeds = self.drivetrain.toWheelSpeeds(speed)

        hal.leftTankVolts = wheelSpeeds.left
        hal.rightTankVolts = wheelSpeeds.right

        self.odom.update(Rotation2d(hal.gyroAngle), hal.leftTankMorotEncoderValue, hal.rightTankMorotEncoderValue)
