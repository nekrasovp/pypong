"""Velocity value object."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Velocity:
    """Immutable velocity value object."""

    x: float
    y: float

    def __post_init__(self) -> None:
        """Validate velocity values."""
        if not isinstance(self.x, (int, float)):
            msg = "x must be a number"
            raise TypeError(msg)
        if not isinstance(self.y, (int, float)):
            msg = "y must be a number"
            raise TypeError(msg)

