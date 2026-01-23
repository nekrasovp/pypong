"""Score entity."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Score:
    """Score entity tracking player scores."""

    player1: int = 0
    player2: int = 0

    def increment_player1(self) -> None:
        """Increment player 1 score."""
        self.player1 += 1

    def increment_player2(self) -> None:
        """Increment player 2 score."""
        self.player2 += 1

    def reset(self) -> None:
        """Reset both scores to zero."""
        self.player1 = 0
        self.player2 = 0

