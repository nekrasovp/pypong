"""Game play scene."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.application.services.game_service import GameService
from pypong.infrastructure.config import (
    BALL_SPEED,
    FPS,
    PADDLE_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from pypong.infrastructure.input.pygame_input_handler import PygameInputHandler
from pypong.infrastructure.rendering.pygame_renderer import PygameRenderer
from pypong.presentation.scenes.base_scene import BaseScene


class GameScene(BaseScene):
    """Game play scene."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
    ) -> None:
        """Initialize game scene."""
        super().__init__(renderer, input_handler)
        # Create game service
        if isinstance(renderer, PygameRenderer) and isinstance(input_handler, PygameInputHandler):
            self.game_service = GameService(
                renderer=renderer,
                input_handler=input_handler,
                screen_width=SCREEN_WIDTH,
                screen_height=SCREEN_HEIGHT,
                ball_speed=BALL_SPEED,
                paddle_speed=PADDLE_SPEED,
            )
        else:
            msg = "GameScene requires PygameRenderer and PygameInputHandler"
            raise TypeError(msg)

        self.last_time: float | None = None
        self.paused = False

    def process_input(self) -> None:
        """Process input events."""
        # Input is handled in game service update
        pass

    def update(self, delta_time: float) -> None:
        """Update game state."""
        if not self.paused:
            actions = self.game_service.update(delta_time)
            if actions.get("quit"):
                # Quit game
                self.switch_to_scene(None)
            elif actions.get("pause"):
                # Pause game - show pause menu
                from pypong.presentation.scenes.pause_scene import PauseScene

                pause_scene = PauseScene(self.renderer, self.input_handler, self)
                self.switch_to_scene(pause_scene)

    def render(self) -> None:
        """Render the game."""
        self.game_service.render()

