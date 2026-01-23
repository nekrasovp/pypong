"""Update game use case."""

from __future__ import annotations

from pypong.application.interfaces.renderer import Renderer
from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.services.ball_physics import BallPhysics
from pypong.domain.services.collision_detector import CollisionDetector
from pypong.domain.services.score_manager import ScoreManager


class UpdateGame:
    """Use case for updating game state."""

    def __init__(
        self,
        screen_width: float,
        screen_height: float,
        ball_speed: float,
    ) -> None:
        """Initialize update game use case.

        Args:
            screen_width: Screen width
            screen_height: Screen height
            ball_speed: Ball speed magnitude
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball_speed = ball_speed

    def execute(
        self,
        ball: Ball,
        player1: Paddle,
        player2: Paddle,
        score: Score,
        delta_time: float,
    ) -> str | None:
        """Execute game update.

        Args:
            ball: Ball entity
            player1: Player 1 paddle
            player2: Player 2 paddle
            score: Score entity
            delta_time: Time elapsed since last update

        Returns:
            'player1_scored' or 'player2_scored' if a point was scored, None otherwise
        """
        # Update ball position
        BallPhysics.update_ball_position(ball, delta_time)

        # Check wall collisions
        BallPhysics.handle_wall_collision(ball, self.screen_width, self.screen_height)

        # Check paddle collisions
        BallPhysics.handle_paddle_collision(ball, player1)
        BallPhysics.handle_paddle_collision(ball, player2)

        # Check if ball is out of bounds (scoring)
        scorer = ScoreManager.check_ball_out_of_bounds(ball, self.screen_width)
        if scorer:
            ScoreManager.update_score(score, scorer)
            BallPhysics.reset_ball(ball, self.screen_width, self.screen_height, self.ball_speed)
            return f"{scorer}_scored"

        return None

