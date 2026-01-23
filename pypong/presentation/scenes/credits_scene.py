"""Credits scene."""

from __future__ import annotations

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.domain.value_objects.color import BLACK, GREY
from pypong.domain.value_objects.position import Position
from pypong.infrastructure.config import SCREEN_HEIGHT, SCREEN_WIDTH
from pypong.presentation.scenes.base_scene import BaseScene


class CreditsScene(BaseScene):
    """Credits scene."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
    ) -> None:
        """Initialize credits scene."""
        super().__init__(renderer, input_handler)
        self.mid_w = SCREEN_WIDTH / 2
        self.mid_h = SCREEN_HEIGHT / 2

    def process_input(self) -> None:
        """Process input events."""
        events = self.input_handler.get_events()

        for event in events:
            if event.is_keydown:
                if event.key == "ESCAPE" or event.key == "RETURN":
                    # Return to main menu
                    from pypong.presentation.scenes.main_menu_scene import MainMenuScene

                    main_menu = MainMenuScene(self.renderer, self.input_handler)
                    self.switch_to_scene(main_menu)

    def update(self, delta_time: float) -> None:
        """Update scene state."""
        # Credits scene doesn't need per-frame updates
        pass

    def render(self) -> None:
        """Render the credits screen."""
        self.renderer.clear(BLACK)

        # Title (centered)
        title_pos = Position(self.mid_w, self.mid_h - 20)
        self.renderer.draw_text("Credits", title_pos, 20, GREY, center=True)

        # Credits text (centered)
        credits_pos = Position(self.mid_w, self.mid_h + 10)
        self.renderer.draw_text("Made by def12", credits_pos, 15, GREY, center=True)

        self.renderer.present()

