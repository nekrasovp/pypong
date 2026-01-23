"""Color value object."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    """Immutable color value object representing RGB color."""

    r: int
    g: int
    b: int

    def __post_init__(self) -> None:
        """Validate color values."""
        if not isinstance(self.r, int) or not (0 <= self.r <= 255):
            msg = "r must be an integer between 0 and 255"
            raise ValueError(msg)
        if not isinstance(self.g, int) or not (0 <= self.g <= 255):
            msg = "g must be an integer between 0 and 255"
            raise ValueError(msg)
        if not isinstance(self.b, int) or not (0 <= self.b <= 255):
            msg = "b must be an integer between 0 and 255"
            raise ValueError(msg)

    def to_tuple(self) -> tuple[int, int, int]:
        """Convert color to RGB tuple."""
        return (self.r, self.g, self.b)


# Common colors
BLACK = Color(0, 0, 0)
GREY = Color(211, 211, 211)
WHITE = Color(255, 255, 255)

