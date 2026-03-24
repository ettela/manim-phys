from manimlib import *

class TDC(Axes):
    def construct(self):
        return super().construct()
class Demo(Scene):
    def construct(self):
        axes = TDC(x_axis_config={"lable": "a"})
        self.add(axes)