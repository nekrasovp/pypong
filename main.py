"""Main entry point for PyPong game."""

import pygame

from pypong.infrastructure.config import SCREEN_HEIGHT, SCREEN_WIDTH
from pypong.infrastructure.input.pygame_input_handler import PygameInputHandler
from pypong.infrastructure.rendering.pygame_renderer import PygameRenderer
from pypong.presentation.controllers.scene_controller import SceneController
from pypong.presentation.scenes.main_menu_scene import MainMenuScene


def main() -> None:
    """Main entry point."""
    # Initialize pygame
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PyPong")

    # Initialize infrastructure
    renderer = PygameRenderer(screen)
    input_handler = PygameInputHandler()

    # Create initial scene
    main_menu = MainMenuScene(renderer, input_handler)

    # Create scene controller
    controller = SceneController(main_menu)

    # Run game
    try:
        controller.run()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
