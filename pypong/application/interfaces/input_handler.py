"""Input handler interface."""

from __future__ import annotations

from typing import Protocol


class InputEvent(Protocol):
    """Input event protocol."""

    @property
    def event_type(self) -> str:
        """Get the event type."""
        ...

    @property
    def key(self) -> str | None:
        """Get the key associated with the event, if any."""
        ...


class InputHandler(Protocol):
    """Interface for input handling."""

    def get_events(self) -> list[InputEvent]:
        """Get all input events since last call.

        Returns:
            List of input events
        """
        ...

    def is_key_pressed(self, key: str) -> bool:
        """Check if a key is currently pressed.

        Args:
            key: Key identifier

        Returns:
            True if key is pressed, False otherwise
        """
        ...

    def should_quit(self) -> bool:
        """Check if quit was requested.

        Returns:
            True if quit requested, False otherwise
        """
        ...

