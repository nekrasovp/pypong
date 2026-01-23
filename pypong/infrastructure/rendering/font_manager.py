"""Font manager for loading and caching fonts."""

from __future__ import annotations

from pathlib import Path

import pygame

from pypong.infrastructure.config import FONT_PATH, FONT_SIZE


class FontManager:
    """Manages font loading and caching."""

    def __init__(self) -> None:
        """Initialize font manager."""
        self._cache: dict[tuple[Path, int], pygame.font.Font] = {}
        self._default_font: pygame.font.Font | None = None

    def get_font(self, path: Path | None = None, size: int = FONT_SIZE) -> pygame.font.Font:
        """Get a font, loading from cache if available.

        Args:
            path: Path to font file, or None for default font
            size: Font size

        Returns:
            Font object
        """
        if path is None:
            if self._default_font is None:
                self._default_font = pygame.font.Font(str(FONT_PATH), size)
            return self._default_font

        cache_key = (path, size)
        if cache_key not in self._cache:
            self._cache[cache_key] = pygame.font.Font(str(path), size)

        return self._cache[cache_key]

