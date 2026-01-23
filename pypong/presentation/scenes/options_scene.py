"""Options menu scene."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.domain.value_objects.color import BLACK, GREY, WHITE
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.infrastructure.config import SCREEN_HEIGHT, SCREEN_WIDTH
from pypong.presentation.scenes.base_scene import BaseScene


class OptionsScene(BaseScene):
    """Options menu scene."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
    ) -> None:
        """Initialize options scene."""
        super().__init__(renderer, input_handler)
        self.state = "Volume"
        self.mid_w = SCREEN_WIDTH / 2
        self.mid_h = SCREEN_HEIGHT / 2
        self.cursor_offset = -100
        self.volume_level = 50  # Volume level (0-100)

    def process_input(self) -> None:
        """Process input events."""
        events = self.input_handler.get_events()

        for event in events:
            if event.is_keydown:
                if event.key == "ESCAPE":
                    # Return to main menu
                    from pypong.presentation.scenes.main_menu_scene import MainMenuScene

                    main_menu = MainMenuScene(self.renderer, self.input_handler)
                    self.switch_to_scene(main_menu)
                elif event.key == "RETURN":
                    # Show details for selected option
                    if self.state == "Volume":
                        # Volume adjustment could go here
                        pass
                    elif self.state == "Controls":
                        # Controls info already shown
                        pass
                elif event.key == "DOWN":
                    # Toggle between options
                    self.state = "Controls" if self.state == "Volume" else "Volume"
                elif event.key == "UP":
                    # Toggle between options
                    self.state = "Volume" if self.state == "Controls" else "Controls"
                elif event.key == "LEFT" and self.state == "Volume":
                    # Decrease volume
                    self.volume_level = max(0, self.volume_level - 10)
                elif event.key == "RIGHT" and self.state == "Volume":
                    # Increase volume
                    self.volume_level = min(100, self.volume_level + 10)

    def update(self, delta_time: float) -> None:
        """Update scene state."""
        # Options menu doesn't need per-frame updates
        pass

    def render(self) -> None:
        """Render the options menu."""
        self.renderer.clear(BLACK)

        # Title (centered)
        title_pos = Position(self.mid_w, self.mid_h - 100)
        self.renderer.draw_text("Options", title_pos, 24, GREY, center=True)

        # Menu items (left-aligned from center)
        menu_x = self.mid_w - 80
        volume_pos = Position(menu_x, self.mid_h - 20)
        controls_pos = Position(menu_x, self.mid_h + 20)

        self.renderer.draw_text("Volume", volume_pos, 18, GREY, center=False)
        self.renderer.draw_text("Controls", controls_pos, 18, GREY, center=False)

        # Cursor (to the left of menu items)
        cursor_x = menu_x + self.cursor_offset
        cursor_y = self.mid_h - 20 if self.state == "Volume" else self.mid_h + 20
        cursor_pos = Position(cursor_x, cursor_y)
        self.renderer.draw_text("*", cursor_pos, 15, GREY, center=False)

        # Show volume level if Volume is selected
        if self.state == "Volume":
            # Volume bar visualization
            volume_text = f"Volume: {self.volume_level}%"
            volume_info_pos = Position(self.mid_w, self.mid_h + 60)
            self.renderer.draw_text(volume_text, volume_info_pos, 16, GREY)
            
            # Volume bar
            bar_width = 300.0
            bar_height = 30.0
            bar_x = self.mid_w - bar_width / 2
            bar_y = self.mid_h + 90
            filled_width = bar_width * self.volume_level / 100
            
            # Draw bar background (outline)
            self.renderer.draw_rect(
                Position(bar_x, bar_y),
                Dimensions(bar_width, bar_height),
                GREY,
            )
            # Draw filled portion
            if filled_width > 0:
                self.renderer.draw_rect(
                    Position(bar_x, bar_y),
                    Dimensions(filled_width, bar_height),
                    WHITE,
                )
            
            help_text = "LEFT/RIGHT: Adjust  |  ESC: Back"
            help_pos = Position(self.mid_w, self.mid_h + 140)
            self.renderer.draw_text(help_text, help_pos, 12, GREY)

        # Show controls info if Controls is selected
        elif self.state == "Controls":
            controls_title_pos = Position(self.mid_w, self.mid_h + 60)
            self.renderer.draw_text("Controls", controls_title_pos, 16, GREY)
            
            controls_info = [
                "Player 1 (AI): Automatic",
                "Player 2: UP/DOWN arrows",
                "ESC: Pause/Return to menu",
                "ENTER: Select",
            ]
            start_y = self.mid_h + 90
            for i, text in enumerate(controls_info):
                info_pos = Position(self.mid_w, start_y + i * 25)
                self.renderer.draw_text(text, info_pos, 14, GREY)
            
            help_text = "ESC: Back to Main Menu"
            help_pos = Position(self.mid_w, self.mid_h + 200)
            self.renderer.draw_text(help_text, help_pos, 12, GREY)

        self.renderer.present()

