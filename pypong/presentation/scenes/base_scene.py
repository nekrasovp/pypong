"""Base scene abstract class."""

from __future__ import annotations

from abc import ABC, abstractmethod

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer


class BaseScene(ABC):
    """Abstract base class for all game scenes."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
    ) -> None:
        """Initialize base scene.

        Args:
            renderer: Renderer interface
            input_handler: Input handler interface
        """
        self.renderer = renderer
        self.input_handler = input_handler
        self._next_scene: BaseScene | None = None
        self._scene_transition_requested = False

    @abstractmethod
    def process_input(self) -> None:
        """Process input events."""
        ...

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Update scene state.

        Args:
            delta_time: Time elapsed since last update
        """
        ...

    @abstractmethod
    def render(self) -> None:
        """Render the scene."""
        ...

    def switch_to_scene(self, scene: BaseScene | None) -> None:
        """Switch to another scene.

        Args:
            scene: Scene to switch to, or None to quit
        """
        self._next_scene = scene
        self._scene_transition_requested = True

    def get_next_scene(self) -> BaseScene | None:
        """Get the next scene to switch to.

        Returns:
            Next scene or None if quit requested
        """
        return self._next_scene
    
    def has_transition_requested(self) -> bool:
        """Check if a scene transition has been requested.
        
        Returns:
            True if transition requested, False otherwise
        """
        return self._scene_transition_requested
    
    def clear_transition_flag(self) -> None:
        """Clear the transition request flag."""
        self._scene_transition_requested = False

