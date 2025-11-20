import wpilib
import rev
import djoAuto
from rev import SparkMax
from ntcore import NetworkTableInstance, NetworkTable

from pathplannerlib.path import PathPlannerPath, PathPlannerTrajectory
from pathplannerlib.config import RobotConfig, ModuleConfig, DCMotor
from wpimath import units
from wpimath.geometry import Translation2d, Pose2d, Rotation2d
from wpimath.kinematics import ChassisSpeeds


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        oneftInMeters = units.feetToMeters(1)
        mass = units.lbsToKilograms(122)
        moi = (  # moi = 1/6 * m * side_in_meters^2 , for a cube 32x32inches :
            (1 / 6.0)
            * mass
            * (32.0 / 12.0 * oneftInMeters)
            * (32.0 / 12.0 * oneftInMeters)
        )
        motor = DCMotor(12, 2.6, 105, 1.8, 594.39, 1)  # old RPM = 5676
        modConfig = ModuleConfig(0.05, 1.1, 1.5, motor, 42, 1)  # old COF = 9.5
        m = DCMotor(12, 2.6, 105, 1.8, 594.39, 1)  # old RPM = 5676

        traj = PathPlannerTrajectory(
            path=PathPlannerPath.fromPathFile("test"),
            starting_speeds=ChassisSpeeds(0, 0),
            starting_rotation=Rotation2d(0),
            config=RobotConfig(
                massKG=mass,
                MOI=moi,
                moduleConfig=ModuleConfig(
                    wheelRadiusMeters=0.05,
                    maxDriveVelocityMPS=1.1,
                    wheelCOF=1.5,
                    driveMotor=motor,
                    driveCurrentLimit=42,
                    numMotors=1,
                ),
                moduleOffsets=[
                    Translation2d(-oneftInMeters, oneftInMeters),
                    Translation2d(oneftInMeters, oneftInMeters),
                    Translation2d(-oneftInMeters, -oneftInMeters),
                    Translation2d(oneftInMeters, -oneftInMeters),
                ],
            ),
        )
        print(traj.getTotalTimeSeconds())
        breakpoint()

        RConfig = RobotConfig(
            mass,
            moi,
            modConfig,
            [
                Translation2d(-oneftInMeters, oneftInMeters),
                Translation2d(oneftInMeters, oneftInMeters),
                Translation2d(-oneftInMeters, -oneftInMeters),
                Translation2d(oneftInMeters, -oneftInMeters),
            ],
        )
        p = PathPlannerPath.fromPathFile("test")
        myTraj = p.generateTrajectory(
            starting_speeds=ChassisSpeeds(0, 0),  # starting speeds = 0 in x,y,rot
            starting_rotation=Rotation2d(0),
            # p.getStartingHolonomicPose().rotation(),
            config=RConfig,
        )
        print(myTraj.getTotalTimeSeconds())
        breakpoint()

        nextTrajState = myTraj.sample(1.3)
        print(nextTrajState.timeSeconds)
        print(myTraj.getState(4).timeSeconds)

        initialPose = Pose2d(
            myTraj.getInitialPose().translation(),
            nextTrajState.holonomicRotation,
        )
        breakpoint()

        self.driveCtrlr = wpilib.XboxController(0)

        self.Motor = SparkMax(2, rev.SparkMax.MotorType.kBrushless)
        self.Motor.set(0)

        self.myOneAutoStage = djoAuto.myCustomAS(5)
        self.myTwoAutoStage = djoAuto.myCustomAS(10)

        auto1_start = djoAuto.myCustomAS(10)
        auto1_shoot = djoAuto.myCustomAS(5)
        auto1_moveBack = djoAuto.myCustomAS(2)
        auto1_allStop = djoAuto.allStopAS()
        auto1_start.setNext(auto1_shoot)
        auto1_shoot.setNext(auto1_moveBack)
        auto1_moveBack.setNext(auto1_allStop)

        trajTest_start = djoAuto.FiddleWithTrajAS()

        self.curAutoStage = trajTest_start
        self.table = NetworkTableInstance.getDefault().getTable("telemetry")

    def robotPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.curAutoStage.autoInit(self)
        self.table.putNumber("test", 2)
        pass

    def autonomousPeriodic(self):
        if self.curAutoStage.isDone(self) == False:
            self.curAutoStage.run(self)
        else:
            self.curAutoStage = self.curAutoStage.getNext(self)
            self.table.putString("NextStage", self.curAutoStage.getNext(self).name)

            self.curAutoStage.autoInit(self)
        pass

    def teleopInit(self) -> None:

        self.on = False

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

    # self.autoDict = {
    #     "stage2": djoAuto.myCustomAS(10, "stage3"),
    #     "stage1": djoAuto.myCustomAS(5, "stage2"),
    #     "stage3": self.myOneAutoStage,
    #     # "stageN": djoAuto.MoveToShoot(
    #     #     "../paths/mypath.json", "stageIDforInPos", "stageIDforOutPos"
    #     # ),
    # }

    # self.autos = {"three piece", forward}
    # self.ThreePiece = forward
    # self.curAutoStage = self.autoDict["stage1"]

    # # self.autoDictionary["stage3"] = djoAuto.myCustomAS(2)
