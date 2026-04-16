import re
from typing import Annotated, Dict, Iterable, Literal, Tuple, Union

import numpy as np
from colour import Color

type ManimColor = Union[str, Color, None]
type RangeSpecifier = Tuple[float, float, float] | Tuple[float, float]

type Span = tuple[int, int]
type SingleSelector = Union[
    str,
    re.Pattern,
    tuple[Union[int, None], Union[int, None]],
]
type Selector = Union[SingleSelector, Iterable[SingleSelector]]

type UniformDict = Dict[str, float | bool | np.ndarray | tuple]

# type FloatArray = np.ndarray[int, np.dtype[np.float64]]
type FloatArray = np.ndarray[tuple[int], np.dtype[np.float64]]
type Vect2 = Annotated[FloatArray, Literal[2]]
type Vect3 = Annotated[FloatArray, Literal[3]]
type Vect4 = Annotated[FloatArray, Literal[4]]
type VectN = Annotated[FloatArray, Literal["N"]]
type Matrix3x3 = Annotated[FloatArray, Literal[3, 3]]
type VectArray = Annotated[FloatArray, Literal["N", 1]]
type Vect2Array = Annotated[FloatArray, Literal["N", 2]]
type Vect3Array = Annotated[FloatArray, Literal["N", 3]]
type Vect4Array = Annotated[FloatArray, Literal["N", 4]]
type VectNArray = Annotated[FloatArray, Literal["N", "M"]]
