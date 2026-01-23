"""Ball entity."""

from __future__ import annotations

from dataclasses import dataclass

from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


@dataclass
class Ball:
    """Ball entity representing the game ball."""

    position: Position
    velocity: Velocity
    dimensions: Dimensions

    def move(self, delta_time: float) -> None:
        """Update ball position based on velocity and delta time."""
        self.position = Position(
            self.position.x + self.velocity.x * delta_time,
            self.position.y + self.velocity.y * delta_time,
        )

    def reverse_x_velocity(self) -> None:
        """Reverse the x component of velocity."""
        self.velocity = Velocity(-self.velocity.x, self.velocity.y)

    def reverse_y_velocity(self) -> None:
        """Reverse the y component of velocity."""
        self.velocity = Velocity(self.velocity.x, -self.velocity.y)

    def set_velocity(self, velocity: Velocity) -> None:
        """Set the ball's velocity."""
        self.velocity = velocity

