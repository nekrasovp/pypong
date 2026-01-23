"""Scene manager service."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pypong.presentation.scenes.base_scene import BaseScene


class SceneManager:
    """Service for managing scene transitions."""

    def __init__(self, initial_scene: BaseScene) -> None:
        """Initialize scene manager.

        Args:
            initial_scene: Initial scene to start with
        """
        self.current_scene: BaseScene | None = initial_scene
        self.next_scene: BaseScene | None = None

    def update(self) -> bool:
        """Update scene manager and handle transitions.

        Returns:
            True if should continue, False if should quit
        """
        if self.current_scene is None:
            return False

        # Check for scene transition
        if self.next_scene is not None:
            self.current_scene = self.next_scene
            self.next_scene = None

        return True

    def switch_scene(self, scene: BaseScene | None) -> None:
        """Switch to a new scene.

        Args:
            scene: Scene to switch to, or None to quit
        """
        if scene is None:
            # Quit requested - set current scene to None
            self.current_scene = None
            self.next_scene = None
        else:
            self.next_scene = scene

    def get_current_scene(self) -> BaseScene | None:
        """Get current scene.

        Returns:
            Current scene or None
        """
        return self.current_scene

