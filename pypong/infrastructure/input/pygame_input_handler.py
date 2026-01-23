"""Pygame input handler implementation."""

from __future__ import annotations

from dataclasses import dataclass

import pygame

from pypong.application.interfaces.input_handler import InputHandler


@dataclass
class PygameInputEvent:
    """Pygame input event wrapper."""

    event_type: str
    key: str | None = None

    @property
    def is_keydown(self) -> bool:
        """Check if this is a keydown event."""
        return self.event_type == "KEYDOWN"

    @property
    def is_keyup(self) -> bool:
        """Check if this is a keyup event."""
        return self.event_type == "KEYUP"


class PygameInputHandler:
    """Pygame implementation of InputHandler interface."""

    # Key mapping from pygame keys to string identifiers
    KEY_MAP: dict[int, str] = {
        pygame.K_UP: "UP",
        pygame.K_DOWN: "DOWN",
        pygame.K_LEFT: "LEFT",
        pygame.K_RIGHT: "RIGHT",
        pygame.K_ESCAPE: "ESCAPE",
        pygame.K_RETURN: "RETURN",
        pygame.K_SPACE: "SPACE",
    }

    def __init__(self) -> None:
        """Initialize pygame input handler."""
        self._should_quit = False
        self._pressed_keys: set[str] = set()

    def get_events(self) -> list[PygameInputEvent]:
        """Get all input events since last call."""
        events: list[PygameInputEvent] = []
        pygame_events = pygame.event.get()

        for event in pygame_events:
            if event.type == pygame.QUIT:
                self._should_quit = True
            elif event.type == pygame.KEYDOWN:
                key_str = self._pygame_key_to_string(event.key)
                if key_str:
                    events.append(PygameInputEvent("KEYDOWN", key_str))
                    self._pressed_keys.add(key_str)
            elif event.type == pygame.KEYUP:
                key_str = self._pygame_key_to_string(event.key)
                if key_str:
                    events.append(PygameInputEvent("KEYUP", key_str))
                    self._pressed_keys.discard(key_str)

        return events

    def is_key_pressed(self, key: str) -> bool:
        """Check if a key is currently pressed."""
        return key in self._pressed_keys

    def should_quit(self) -> bool:
        """Check if quit was requested."""
        return self._should_quit

    def _pygame_key_to_string(self, pygame_key: int) -> str | None:
        """Convert pygame key constant to string identifier."""
        return self.KEY_MAP.get(pygame_key)

