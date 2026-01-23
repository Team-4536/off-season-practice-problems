import wpilib
import rev

# step 1: define an xbox controller with the name mechCtrl and the id of 1
# step 2: define a sparkMax motor with the ID of 1 and brushless value for type
# step 3: in teleop, make an if else statement that checks if the a button is pressed on mechCtrl
# step 4 bro: when a is pressed, set motor voltage to 1. if not pressed, set motor voltage to zero
# use wpilib docs and rev docs to find out how to define them


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.mechCtrl = wpilib.XboxController(1)
        self.motor = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushless)

        self.motor.setVoltage(0)

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self):
        if self.mechCtrl.getAButton():
            self.motor.setVoltage(1)
        else:
            self.motor.setVoltage(0)


if __name__ == "__main__":
    wpilib.run(Robot)
