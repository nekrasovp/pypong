"""Renderer interface."""

from __future__ import annotations

from typing import Protocol

from pypong.domain.value_objects.color import Color
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position


class Renderer(Protocol):
    """Interface for rendering operations."""

    def clear(self, color: Color) -> None:
        """Clear the screen with the specified color.

        Args:
            color: Color to clear with
        """
        ...

    def draw_rect(
        self,
        position: Position,
        dimensions: Dimensions,
        color: Color,
    ) -> None:
        """Draw a rectangle.

        Args:
            position: Top-left position of rectangle
            dimensions: Width and height of rectangle
            color: Color of rectangle
        """
        ...

    def draw_circle(
        self,
        position: Position,
        radius: float,
        color: Color,
    ) -> None:
        """Draw a circle.

        Args:
            position: Center position of circle
            radius: Radius of circle
            color: Color of circle
        """
        ...

    def draw_line(
        self,
        start: Position,
        end: Position,
        color: Color,
    ) -> None:
        """Draw a line.

        Args:
            start: Start position
            end: End position
            color: Color of line
        """
        ...

    def draw_text(
        self,
        text: str,
        position: Position,
        font_size: int,
        color: Color,
        center: bool = True,
    ) -> None:
        """Draw text on screen.

        Args:
            text: Text to draw
            position: Position to draw text at (center if center=True, top-left if center=False)
            font_size: Size of font
            color: Color of text
            center: If True, position is treated as center; if False, as top-left
        """
        ...

    def present(self) -> None:
        """Present the rendered frame to the screen."""
        ...

    def get_screen_dimensions(self) -> Dimensions:
        """Get screen dimensions.

        Returns:
            Screen dimensions
        """
        ...

