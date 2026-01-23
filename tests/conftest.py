"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_position():
    """Create a sample position."""
    from pypong.domain.value_objects.position import Position

    return Position(100.0, 200.0)


@pytest.fixture
def sample_velocity():
    """Create a sample velocity."""
    from pypong.domain.value_objects.velocity import Velocity

    return Velocity(5.0, -3.0)


@pytest.fixture
def sample_dimensions():
    """Create sample dimensions."""
    from pypong.domain.value_objects.dimensions import Dimensions

    return Dimensions(30.0, 30.0)


@pytest.fixture
def sample_ball(sample_position, sample_velocity, sample_dimensions):
    """Create a sample ball."""
    from pypong.domain.entities.ball import Ball

    return Ball(
        position=sample_position,
        velocity=sample_velocity,
        dimensions=sample_dimensions,
    )


@pytest.fixture
def sample_paddle(sample_position, sample_dimensions):
    """Create a sample paddle."""
    from pypong.domain.entities.paddle import Paddle

    return Paddle(
        position=sample_position,
        dimensions=sample_dimensions,
        speed=7.0,
    )


@pytest.fixture
def sample_score():
    """Create a sample score."""
    from pypong.domain.entities.score import Score

    return Score()

