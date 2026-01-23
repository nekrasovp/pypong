"""Handle input use case."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.domain.entities.paddle import Paddle


class HandleInput:
    """Use case for handling input."""

    def __init__(
        self,
        input_handler: InputHandler,
        screen_height: float,
    ) -> None:
        """Initialize handle input use case.

        Args:
            input_handler: Input handler interface
            screen_height: Screen height for boundary checking
        """
        self.input_handler = input_handler
        self.screen_height = screen_height

    def execute(
        self,
        player2: Paddle,
        delta_time: float,
    ) -> dict[str, bool]:
        """Execute input handling.

        Args:
            player2: Player 2 paddle (human controlled)
            delta_time: Time elapsed since last update

        Returns:
            Dictionary with action flags (e.g., {'quit': False, 'pause': False})
        """
        actions: dict[str, bool] = {
            "quit": False,
            "pause": False,
        }

        # Check for quit
        if self.input_handler.should_quit():
            actions["quit"] = True
            return actions

        # Handle player 2 movement
        if self.input_handler.is_key_pressed("DOWN"):
            player2.move_down(delta_time, self.screen_height)
        if self.input_handler.is_key_pressed("UP"):
            player2.move_up(delta_time)

        # Check for pause (ESC key)
        events = self.input_handler.get_events()
        for event in events:
            if event.is_keydown and event.key == "ESCAPE":
                actions["pause"] = True

        return actions

