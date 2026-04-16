from keep_project_name.model.state.meta import Field, Mass, Shape, SpaceTime, Velocity

__all__ = ["MetaState"]


class MetaState:
    def __init__(self):
        self.mass: Mass = Mass()
        self.shapes: Shape = Shape()
        self.space_time: SpaceTime = SpaceTime()
        self.velocity: Velocity = Velocity()
        self.field: Field = Field()
