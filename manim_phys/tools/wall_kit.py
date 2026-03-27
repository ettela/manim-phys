from manimlib import *


class WallKit(Line):
    def __init__(self, choice: list[str, int] |None = None, **kwargs):
        self.choice = choice
        if choice[0] == "h":
            self.weight = choice[1]
            arg = self.weight * RIGHT
        elif choice[0] == "v":
            self.height = choice[1]
            arg = self.height * UP

        Line.__init__(self, ORIGIN, arg, **kwargs)
        self.tick_spacing = 0.5
        self.tick_length = 0.25
        self.tick_style = {
            "stroke_width": 1,
            "stroke_color": self.color,
        }

        self.ticks = self.get_ticks()
        self.add(self.ticks)

    def draw_ticks(self, worh):
        if self.choice[0] == "h":
            sop_style = [DL, RIGHT, UL]
        elif self.choice[0] == "v":
            sop_style = [UR, UP, DR]
        n_lines = int(worh / self.tick_spacing)
        lines = VGroup(
            *[
                Line(ORIGIN, self.tick_length * sop_style[0]).shift(
                    (n + 1) * self.tick_spacing * sop_style[1]
                )
                for n in range(n_lines)
            ]
        )
        lines.set_style(**self.tick_style)
        lines.move_to(self, sop_style[2])
        return lines

    def get_ticks(self):
        if self.choice[0] == "h":
            worh = self.weight
        elif self.choice[0] == "v":
            worh = self.height
        return self.draw_ticks(worh)
