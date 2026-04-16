from keep_project_name.model.state.meta.field import Field
from keep_project_name.model.state.meta.mass import Mass
from keep_project_name.model.state.meta.shapes import Shape
from keep_project_name.model.state.meta.space_time import SpaceTime
from keep_project_name.model.state.meta.velocity import Velocity


class MetaState:
    def __init__(self):
        self.mass: Mass = Mass()
        self.shapes: Shape = Shape()
        self.space_time: SpaceTime = SpaceTime()
        self.velocity: Velocity = Velocity()
        self.field: Field = Field()


if __name__ == "__main__":
    print(type(Mass))
