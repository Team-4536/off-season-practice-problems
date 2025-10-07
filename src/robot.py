import wpilib
import rev
import djoAuto
from rev import SparkMax


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:

        self.driveCtrlr = wpilib.XboxController(0)

        self.Motor = SparkMax(2, rev.SparkMax.MotorType.kBrushless)

        self.Motor.set(0)
        self.myOneAutoStage = djoAuto.myCustomAS(5)
        self.myTwoAutoStage = djoAuto.myCustomAS(10)

        self.autoDict = {
            "stage1": djoAuto.myCustomAS(5),
            "stage2": djoAuto.myCustomAS(10),
            "stage3": self.myOneAutoStage,
        }
        self.curAutoStage = self.autoDict["stage1"]

        # self.autoDictionary["stage3"] = djoAuto.myCustomAS(2)

    def robotPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.curAutoStage.autoInit(self)
        pass

    def autonomousPeriodic(self):
        if self.curAutoStage.isDone(self) == False:
            self.curAutoStage.run(self)
        else:
            nextStageID = self.curAutoStage.getNext(self)
            curAutoStage = self.autoDict[nextStageID]
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
