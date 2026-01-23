"""Score management service."""

from __future__ import annotations

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.score import Score


class ScoreManager:
    """Service for managing game scoring."""

    @staticmethod
    def check_ball_out_of_bounds(
        ball: Ball,
        screen_width: float,
    ) -> str | None:
        """Check if ball is out of bounds and which player scored.

        Args:
            ball: The ball entity
            screen_width: Screen width

        Returns:
            'player1' if player 1 scored, 'player2' if player 2 scored, None otherwise
        """
        if ball.position.x <= 0:
            return "player2"
        if ball.position.x + ball.dimensions.width >= screen_width:
            return "player1"
        return None

    @staticmethod
    def update_score(score: Score, scorer: str) -> None:
        """Update score based on who scored.

        Args:
            score: The score entity
            scorer: 'player1' or 'player2'
        """
        if scorer == "player1":
            score.increment_player1()
        elif scorer == "player2":
            score.increment_player2()
        else:
            msg = f"Invalid scorer: {scorer}"
            raise ValueError(msg)

    @staticmethod
    def reset_score(score: Score) -> None:
        """Reset the score to zero.

        Args:
            score: The score entity to reset
        """
        score.reset()

