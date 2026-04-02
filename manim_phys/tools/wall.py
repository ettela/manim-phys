from manimlib.constants import *
from manimlib.mobject.geometry import Line
from manimlib.mobject.types.vectorized_mobject import VGroup

from manim_phys.manim_types import *


class CWall(Line):
    _M_L = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    _M_S = np.array(
        [
            [-1 / np.sqrt(2), -1 / np.sqrt(2), 0],
            [1 / np.sqrt(2), -1 / np.sqrt(2), 0],
            [0, 0, 1],
        ]
    )
    _M_F = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])

    def __init__(
        self,
        start: Vect3 = ORIGIN,
        facing: Vect3 = UP,
        length: float = 1.0,
        flip_ticks: bool = False,
        **kwargs,
    ):
        self._start = start

        _norm = np.linalg.norm(facing)
        if _norm == 0:
            raise ValueError("Facing vector cannot be the zero vector.")
        self.facing = facing / _norm

        self._length = length
        Line.__init__(
            self,
            start=self._start,
            end=self._length * (self.facing @ self._M_L),
            **kwargs,
        )
        # TODO:: style method
        self._tick_spacing = 0.5
        self._tick_length = 0.25
        self._tick_style = {
            "stroke_width": 1,
            "stroke_color": self.color,
        }
        self._filp_ticks = flip_ticks

        self.ticks = self.get_ticks()
        self.add(self.ticks)

    def get_ticks(self):
        vec_t = self.facing @ self._M_S
        if self._filp_ticks:
            vec_t = vec_t @ self._M_F

        n_lines = int(self._length / self._tick_spacing)

        lines = VGroup(
            *[
                Line(ORIGIN, self._tick_length * vec_t).shift(
                    (n + 1) * self._tick_spacing * (self.facing @ self._M_L)
                )
                for n in range(n_lines)
            ]
        )
        lines.set_style(**self._tick_style)
        lines.move_to(self, self.facing)
        return lines
