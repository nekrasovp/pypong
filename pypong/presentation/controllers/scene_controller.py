"""Scene controller for managing game loop."""

from __future__ import annotations

import time

import pygame

from pypong.application.services.scene_manager import SceneManager
from pypong.infrastructure.config import FPS
from pypong.presentation.scenes.base_scene import BaseScene


class SceneController:
    """Controller for managing scene lifecycle and game loop."""

    def __init__(self, initial_scene: BaseScene) -> None:
        """Initialize scene controller.

        Args:
            initial_scene: Initial scene to start with
        """
        self.scene_manager = SceneManager(initial_scene)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """Run the game loop."""
        last_time = time.time()

        while self.running:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time

            # Update scene manager
            if not self.scene_manager.update():
                self.running = False
                break

            current_scene = self.scene_manager.get_current_scene()
            if current_scene is None:
                self.running = False
                break

            # Check for quit from input handler (X button)
            if hasattr(current_scene, "input_handler"):
                if current_scene.input_handler.should_quit():
                    self.running = False
                    break

            # Process input
            current_scene.process_input()

            # Update scene
            current_scene.update(delta_time)

            # Render scene
            current_scene.render()

            # Check for scene transition
            if current_scene.has_transition_requested():
                next_scene = current_scene.get_next_scene()
                # If next_scene is None, it means quit was requested
                if next_scene is None:
                    self.running = False
                    break
                self.scene_manager.switch_scene(next_scene)
                current_scene.clear_transition_flag()

            # Tick clock
            self.clock.tick(FPS)

