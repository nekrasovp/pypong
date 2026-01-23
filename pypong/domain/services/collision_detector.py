"""Collision detection service."""

from __future__ import annotations

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle


class CollisionDetector:
    """Service for detecting collisions between game entities."""

    @staticmethod
    def ball_paddle_collision(ball: Ball, paddle: Paddle, threshold: float = 10.0) -> bool:
        """Check if ball collides with paddle.

        Args:
            ball: The ball entity
            paddle: The paddle entity
            threshold: Minimum overlap distance to consider collision

        Returns:
            True if collision detected, False otherwise
        """
        ball_left = ball.position.x
        ball_right = ball.position.x + ball.dimensions.width
        ball_top = ball.position.y
        ball_bottom = ball.position.y + ball.dimensions.height

        paddle_left = paddle.position.x
        paddle_right = paddle.position.x + paddle.dimensions.width
        paddle_top = paddle.position.y
        paddle_bottom = paddle.position.y + paddle.dimensions.height

        return (
            ball_right >= paddle_left
            and ball_left <= paddle_right
            and ball_bottom >= paddle_top
            and ball_top <= paddle_bottom
        )

    @staticmethod
    def get_collision_side(
        ball: Ball,
        paddle: Paddle,
        threshold: float = 10.0,
    ) -> str | None:
        """Determine which side of the paddle the ball collided with.

        Args:
            ball: The ball entity
            paddle: The paddle entity
            threshold: Minimum overlap distance to consider collision

        Returns:
            'left', 'right', 'top', 'bottom', or None if no collision
        """
        if not CollisionDetector.ball_paddle_collision(ball, paddle, threshold):
            return None

        ball_left = ball.position.x
        ball_right = ball.position.x + ball.dimensions.width
        ball_top = ball.position.y
        ball_bottom = ball.position.y + ball.dimensions.height

        paddle_left = paddle.position.x
        paddle_right = paddle.position.x + paddle.dimensions.width
        paddle_top = paddle.position.y
        paddle_bottom = paddle.position.y + paddle.dimensions.height

        # Check horizontal collision (left/right)
        if abs(ball_right - paddle_left) < threshold and ball.position.x < paddle.position.x:
            return "left"
        if abs(ball_left - paddle_right) < threshold and ball.position.x > paddle.position.x:
            return "right"

        # Check vertical collision (top/bottom)
        if abs(ball_bottom - paddle_top) < threshold and ball.position.y < paddle.position.y:
            return "top"
        if abs(ball_top - paddle_bottom) < threshold and ball.position.y > paddle.position.y:
            return "bottom"

        return None

    @staticmethod
    def ball_wall_collision(
        ball: Ball,
        screen_width: float,
        screen_height: float,
    ) -> tuple[bool, bool]:
        """Check if ball collides with screen boundaries.

        Args:
            ball: The ball entity
            screen_width: Screen width
            screen_height: Screen height

        Returns:
            Tuple of (horizontal_collision, vertical_collision)
        """
        horizontal = ball.position.x <= 0 or ball.position.x + ball.dimensions.width >= screen_width
        vertical = ball.position.y <= 0 or ball.position.y + ball.dimensions.height >= screen_height
        return (horizontal, vertical)

