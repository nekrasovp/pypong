"""Pause menu scene."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.domain.value_objects.color import BLACK, GREY
from pypong.domain.value_objects.position import Position
from pypong.infrastructure.config import SCREEN_HEIGHT, SCREEN_WIDTH
from pypong.presentation.scenes.base_scene import BaseScene


class PauseScene(BaseScene):
    """Pause menu scene."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
        game_scene: BaseScene,
    ) -> None:
        """Initialize pause scene.

        Args:
            renderer: Renderer interface
            input_handler: Input handler interface
            game_scene: The game scene to return to
        """
        super().__init__(renderer, input_handler)
        self.game_scene = game_scene
        self.state = "Resume"
        self.mid_w = SCREEN_WIDTH / 2
        self.mid_h = SCREEN_HEIGHT / 2
        self.cursor_offset = -100

    def process_input(self) -> None:
        """Process input events."""
        events = self.input_handler.get_events()

        for event in events:
            if event.is_keydown:
                if event.key == "DOWN":
                    self._move_cursor_down()
                elif event.key == "UP":
                    self._move_cursor_up()
                elif event.key == "RETURN":
                    self._handle_selection()
                elif event.key == "ESCAPE":
                    # Resume game on ESC
                    self.switch_to_scene(self.game_scene)

    def _move_cursor_down(self) -> None:
        """Move cursor down."""
        if self.state == "Resume":
            self.state = "Quit"
        elif self.state == "Quit":
            self.state = "Resume"

    def _move_cursor_up(self) -> None:
        """Move cursor up."""
        if self.state == "Resume":
            self.state = "Quit"
        elif self.state == "Quit":
            self.state = "Resume"

    def _handle_selection(self) -> None:
        """Handle menu selection."""
        if self.state == "Resume":
            # Return to game
            self.switch_to_scene(self.game_scene)
        elif self.state == "Quit":
            # Return to main menu
            from pypong.presentation.scenes.main_menu_scene import MainMenuScene

            main_menu = MainMenuScene(self.renderer, self.input_handler)
            self.switch_to_scene(main_menu)

    def update(self, delta_time: float) -> None:
        """Update scene state."""
        # Pause menu doesn't need per-frame updates
        pass

    def render(self) -> None:
        """Render the pause menu."""
        self.renderer.clear(BLACK)

        # Title (centered)
        title_pos = Position(self.mid_w, self.mid_h - 40)
        self.renderer.draw_text("PAUSED", title_pos, 24, GREY, center=True)

        # Menu items (left-aligned from center)
        menu_x = self.mid_w - 80
        resume_pos = Position(menu_x, self.mid_h + 20)
        quit_pos = Position(menu_x, self.mid_h + 40)

        self.renderer.draw_text("Resume", resume_pos, 20, GREY, center=False)
        self.renderer.draw_text("Quit to Menu", quit_pos, 20, GREY, center=False)

        # Cursor (to the left of menu items)
        cursor_x = menu_x + self.cursor_offset
        cursor_y = self.mid_h + 20 if self.state == "Resume" else self.mid_h + 40
        cursor_pos = Position(cursor_x, cursor_y)
        self.renderer.draw_text("*", cursor_pos, 15, GREY, center=False)

        self.renderer.present()

