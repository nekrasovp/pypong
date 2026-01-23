"""Pygame renderer implementation."""

from __future__ import annotations

import pygame

from pypong.application.interfaces.renderer import Renderer
from pypong.domain.value_objects.color import Color
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.infrastructure.rendering.font_manager import FontManager


class PygameRenderer:
    """Pygame implementation of Renderer interface."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize pygame renderer.

        Args:
            screen: Pygame surface to render to
        """
        self.screen = screen
        self.font_manager = FontManager()

    def clear(self, color: Color) -> None:
        """Clear the screen with the specified color."""
        self.screen.fill(color.to_tuple())

    def draw_rect(
        self,
        position: Position,
        dimensions: Dimensions,
        color: Color,
    ) -> None:
        """Draw a rectangle."""
        rect = pygame.Rect(
            int(position.x),
            int(position.y),
            int(dimensions.width),
            int(dimensions.height),
        )
        pygame.draw.rect(self.screen, color.to_tuple(), rect)

    def draw_circle(
        self,
        position: Position,
        radius: float,
        color: Color,
    ) -> None:
        """Draw a circle."""
        pygame.draw.circle(
            self.screen,
            color.to_tuple(),
            (int(position.x), int(position.y)),
            int(radius),
        )

    def draw_line(
        self,
        start: Position,
        end: Position,
        color: Color,
    ) -> None:
        """Draw a line."""
        pygame.draw.aaline(
            self.screen,
            color.to_tuple(),
            (int(start.x), int(start.y)),
            (int(end.x), int(end.y)),
        )

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
            position: Position (center if center=True, top-left if center=False)
            font_size: Font size
            color: Text color
            center: If True, position is treated as center; if False, as top-left
        """
        font = self.font_manager.get_font(size=font_size)
        text_surface = font.render(text, False, color.to_tuple())
        if center:
            # Center the text
            text_rect = text_surface.get_rect(center=(int(position.x), int(position.y)))
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (int(position.x), int(position.y)))

    def present(self) -> None:
        """Present the rendered frame to the screen."""
        pygame.display.flip()

    def get_screen_dimensions(self) -> Dimensions:
        """Get screen dimensions."""
        width, height = self.screen.get_size()
        return Dimensions(float(width), float(height))

