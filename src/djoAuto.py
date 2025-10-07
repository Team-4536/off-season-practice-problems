import robot
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from robot import Robot


class AutoStage:
    def __init__(self):
        # This is the constructor (startup code), declare your variables here.
        # It will be called when the robot starts.
        pass

    def run(self, r: "Robot"):
        # this will be called repeatedly every 20ms (e.g., loop())
        pass

    def isDone(self, r: "Robot") -> bool:
        # this will be called at the end of the run() and if it returns true will stop the stage
        return True

    def autoInit(self, r: "Robot"):
        # This is similar to __init__ but it will be called when Auto Begins, it is useful for
        # resetting encode positions or reseting gyros, etc.  Anything that should be reset each
        # auto run. (e.g., when running Auto on the practice field.)
        pass

    def getNext(self, r: "Robot"):
        # This Function contains a string that indicates which stage runs next. It must match
        # those strings created in robot.py (TOOD: Find a better way to link strings to AS objs.)
        return "stage2"
        pass


class myCustomAS(AutoStage):
    def __init__(self, numSec: float = 20):
        self.myCounter = 5 * numSec  # 20ms per cycle, 50 cycles = 1 second
        pass

    def run(self, r: "Robot"):
        self.myCounter = self.myCounter - 1
        r.Motor.set(0.2)

        pass

    def isDone(self, r: "Robot") -> bool:
        if self.myCounter <= 0:
            r.Motor.set(0.0)
            return False
        return True

    def autoInit(self, r: "Robot"):
        pass


## TODO: add an example similar to above, but remove counter and use Timer Class.
## TODO: Decide on a datastructure (dictionary?) and implement a (branching?) queue system.
#          If its branching...makes sure to do a simple non-branching example first.
