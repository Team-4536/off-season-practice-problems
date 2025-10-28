import wpilib
import simHAL
from robotHAL import RobotHAL, RobotHALBuffer
from timing import TimeData


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        if self.isSimulation:
            self.RobotHAL = simHAL.RobotSimHAL()
        else:
            self.buf = RobotHALBuffer()
            self.RobotHAL = RobotHAL()

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self):
        # motor forwards (y) and backwards (b)
        if self.buf.yButton:
            self.buf.motorOneVolts = 0.2
        else:
            self.buf.motorOneVolts = 0

        if self.buf.bButton:
            self.buf.motorOneVolts = -0.2
        else:
            self.buf.motorOneVolts = 0

        # motor two forwards (x) and backwards (a)
        if self.buf.xButton:
            self.buf.motorTwoVolts = 0.2
        else:
            self.buf.motorTwoVolts = 0

        if self.buf.aButton:
            self.buf.motorTwoVolts = -0.2
        else:
            self.buf.motorTwoVolts = 0


if __name__ == "__main__":
    wpilib.run(Robot)
