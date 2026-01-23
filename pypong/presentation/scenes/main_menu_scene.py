"""Main menu scene."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.domain.value_objects.color import BLACK, GREY
from pypong.domain.value_objects.position import Position
from pypong.infrastructure.config import SCREEN_HEIGHT, SCREEN_WIDTH
from pypong.presentation.scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    """Main menu scene."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
    ) -> None:
        """Initialize main menu scene."""
        super().__init__(renderer, input_handler)
        self.state = "Start"
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

    def _move_cursor_down(self) -> None:
        """Move cursor down."""
        if self.state == "Start":
            self.state = "Options"
        elif self.state == "Options":
            self.state = "Credits"
        elif self.state == "Credits":
            self.state = "Quit"
        elif self.state == "Quit":
            self.state = "Start"

    def _move_cursor_up(self) -> None:
        """Move cursor up."""
        if self.state == "Start":
            self.state = "Quit"
        elif self.state == "Options":
            self.state = "Start"
        elif self.state == "Credits":
            self.state = "Options"
        elif self.state == "Quit":
            self.state = "Credits"

    def _handle_selection(self) -> None:
        """Handle menu selection."""
        if self.state == "Start":
            # Switch to game scene
            from pypong.presentation.scenes.game_scene import GameScene

            game_scene = GameScene(self.renderer, self.input_handler)
            self.switch_to_scene(game_scene)
        elif self.state == "Options":
            # Switch to options scene
            from pypong.presentation.scenes.options_scene import OptionsScene

            options_scene = OptionsScene(self.renderer, self.input_handler)
            self.switch_to_scene(options_scene)
        elif self.state == "Credits":
            # Switch to credits scene
            from pypong.presentation.scenes.credits_scene import CreditsScene

            credits_scene = CreditsScene(self.renderer, self.input_handler)
            self.switch_to_scene(credits_scene)
        elif self.state == "Quit":
            # Quit game
            self.switch_to_scene(None)

    def update(self, delta_time: float) -> None:
        """Update scene state."""
        # Menu doesn't need per-frame updates
        pass

    def render(self) -> None:
        """Render the menu."""
        self.renderer.clear(BLACK)

        # Title (centered)
        title_pos = Position(self.mid_w, self.mid_h - 20)
        self.renderer.draw_text("Main Menu", title_pos, 20, GREY, center=True)

        # Menu items (left-aligned from center)
        menu_x = self.mid_w - 80  # Offset from center for left alignment
        start_pos = Position(menu_x, self.mid_h + 20)
        options_pos = Position(menu_x, self.mid_h + 40)
        credits_pos = Position(menu_x, self.mid_h + 60)
        quit_pos = Position(menu_x, self.mid_h + 80)

        self.renderer.draw_text("Start Game", start_pos, 20, GREY, center=False)
        self.renderer.draw_text("Options", options_pos, 20, GREY, center=False)
        self.renderer.draw_text("Credits", credits_pos, 20, GREY, center=False)
        self.renderer.draw_text("Quit", quit_pos, 20, GREY, center=False)

        # Cursor (to the left of menu items)
        cursor_x = menu_x + self.cursor_offset
        if self.state == "Start":
            cursor_y = self.mid_h + 20
        elif self.state == "Options":
            cursor_y = self.mid_h + 40
        elif self.state == "Credits":
            cursor_y = self.mid_h + 60
        else:  # Quit
            cursor_y = self.mid_h + 80

        cursor_pos = Position(cursor_x, cursor_y)
        self.renderer.draw_text("*", cursor_pos, 15, GREY, center=False)

        self.renderer.present()

