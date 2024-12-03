from robotHAL import RobotHALBuffer

class OneMotorSubsystem():

    def __init__(self) -> None:
        pass

    def update(self, runMotorInput: bool, buf: RobotHALBuffer) -> None:
        if runMotorInput:
            buf.oneMotorVolts = 0.4
        else:
            buf.oneMotorVolts = 0