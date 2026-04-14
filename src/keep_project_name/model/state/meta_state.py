from .meta import *
from .phys_types import *


class MetaState:
    def __init__(self):
        self.mass: Mass = Mass()
        self.shapes: Shape = Shape()
        self.space_time: SpaceTime = SpaceTime()
        self.velocity: Velocity = Velocity()
        self.field: Field = Field()
