"""Dimensions value object."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Dimensions:
    """Immutable dimensions value object."""

    width: float
    height: float

    def __post_init__(self) -> None:
        """Validate dimensions values."""
        if not isinstance(self.width, (int, float)) or self.width <= 0:
            msg = "width must be a positive number"
            raise ValueError(msg)
        if not isinstance(self.height, (int, float)) or self.height <= 0:
            msg = "height must be a positive number"
            raise ValueError(msg)

