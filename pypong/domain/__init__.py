"""Domain layer - pure game logic with no external dependencies."""

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.value_objects.color import Color
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity

__all__ = [
    "Ball",
    "Paddle",
    "Score",
    "Color",
    "Dimensions",
    "Position",
    "Velocity",
]

