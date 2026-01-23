"""Tests for value objects."""

import pytest

from pypong.domain.value_objects.color import Color
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


def test_position_creation():
    """Test position creation."""
    pos = Position(100.0, 200.0)
    assert pos.x == 100.0
    assert pos.y == 200.0


def test_position_immutability():
    """Test that position is immutable."""
    pos = Position(100.0, 200.0)
    with pytest.raises(Exception):  # noqa: PT011
        pos.x = 50.0  # type: ignore[misc]


def test_velocity_creation():
    """Test velocity creation."""
    vel = Velocity(5.0, -3.0)
    assert vel.x == 5.0
    assert vel.y == -3.0


def test_color_creation():
    """Test color creation."""
    color = Color(255, 128, 64)
    assert color.r == 255
    assert color.g == 128
    assert color.b == 64


def test_color_to_tuple():
    """Test color to tuple conversion."""
    color = Color(255, 128, 64)
    assert color.to_tuple() == (255, 128, 64)


def test_color_validation():
    """Test color validation."""
    with pytest.raises(ValueError):
        Color(300, 128, 64)  # r > 255

    with pytest.raises(ValueError):
        Color(255, -10, 64)  # g < 0


def test_dimensions_creation():
    """Test dimensions creation."""
    dims = Dimensions(100.0, 200.0)
    assert dims.width == 100.0
    assert dims.height == 200.0


def test_dimensions_validation():
    """Test dimensions validation."""
    with pytest.raises(ValueError):
        Dimensions(-10.0, 200.0)  # width <= 0

    with pytest.raises(ValueError):
        Dimensions(100.0, 0.0)  # height <= 0

