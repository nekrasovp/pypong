"""Paddle entity."""

from __future__ import annotations

from dataclasses import dataclass

from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position


@dataclass
class Paddle:
    """Paddle entity representing a player's paddle."""

    position: Position
    dimensions: Dimensions
    speed: float

    def move_up(self, delta_time: float, min_y: float = 0.0) -> None:
        """Move paddle up."""
        new_y = self.position.y - self.speed * delta_time
        if new_y < min_y:
            new_y = min_y
        self.position = Position(self.position.x, new_y)

    def move_down(self, delta_time: float, max_y: float) -> None:
        """Move paddle down."""
        new_y = self.position.y + self.speed * delta_time
        max_position = max_y - self.dimensions.height
        if new_y > max_position:
            new_y = max_position
        self.position = Position(self.position.x, new_y)

    def move_to_y(self, target_y: float, min_y: float = 0.0, max_y: float | None = None) -> None:
        """Move paddle to target y position (for AI)."""
        if max_y is not None:
            max_position = max_y - self.dimensions.height
            target_y = min(target_y, max_position)
        target_y = max(target_y, min_y)
        self.position = Position(self.position.x, target_y)

