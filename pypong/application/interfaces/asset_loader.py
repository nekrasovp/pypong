"""Asset loader interface."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol


class Font(Protocol):
    """Font protocol."""

    def render(
        self,
        text: str,
        antialias: bool,
        color: tuple[int, int, int],
    ) -> object:
        """Render text with the font.

        Args:
            text: Text to render
            antialias: Whether to use antialiasing
            color: RGB color tuple

        Returns:
            Rendered surface object
        """
        ...


class AssetLoader(Protocol):
    """Interface for loading game assets."""

    def load_font(self, path: Path, size: int) -> Font:
        """Load a font from file.

        Args:
            path: Path to font file
            size: Font size

        Returns:
            Font object
        """
        ...

