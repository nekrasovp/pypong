"""Ball physics service."""

from __future__ import annotations

import random

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


class BallPhysics:
    """Service for ball physics calculations."""

    @staticmethod
    def update_ball_position(ball: Ball, delta_time: float) -> None:
        """Update ball position based on velocity.

        Args:
            ball: The ball entity to update
            delta_time: Time elapsed since last update
        """
        ball.move(delta_time)

    @staticmethod
    def handle_wall_collision(ball: Ball, screen_width: float, screen_height: float) -> None:
        """Handle ball collision with screen boundaries.

        Args:
            ball: The ball entity
            screen_width: Screen width
            screen_height: Screen height
        """
        if ball.position.y <= 0 or ball.position.y + ball.dimensions.height >= screen_height:
            ball.reverse_y_velocity()

    @staticmethod
    def handle_paddle_collision(ball: Ball, paddle: Paddle, threshold: float = 10.0) -> bool:
        """Handle ball collision with paddle.

        Args:
            ball: The ball entity
            paddle: The paddle entity
            threshold: Minimum overlap distance to consider collision

        Returns:
            True if collision occurred, False otherwise
        """
        from pypong.domain.services.collision_detector import CollisionDetector

        if not CollisionDetector.ball_paddle_collision(ball, paddle, threshold):
            return False

        collision_side = CollisionDetector.get_collision_side(ball, paddle, threshold)

        if collision_side == "left" or collision_side == "right":
            ball.reverse_x_velocity()
        elif collision_side == "top" or collision_side == "bottom":
            ball.reverse_y_velocity()

        return True

    @staticmethod
    def reset_ball(
        ball: Ball,
        screen_width: float,
        screen_height: float,
        speed: float,
    ) -> None:
        """Reset ball to center with random velocity.

        Args:
            ball: The ball entity to reset
            screen_width: Screen width
            screen_height: Screen height
            speed: Ball speed magnitude
        """
        center_x = screen_width / 2 - ball.dimensions.width / 2
        center_y = screen_height / 2 - ball.dimensions.height / 2
        ball.position = Position(center_x, center_y)

        # Random direction
        velocity_x = speed * random.choice((1, -1))
        velocity_y = speed * random.choice((1, -1))
        ball.set_velocity(Velocity(velocity_x, velocity_y))

