"""Tests for application use cases."""

from unittest.mock import Mock

from pypong.application.use_cases.handle_input import HandleInput
from pypong.application.use_cases.update_game import UpdateGame
from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


def test_update_game_execute():
    """Test update game use case."""
    update_game = UpdateGame(1000.0, 800.0, 7.0)

    ball = Ball(
        position=Position(500.0, 400.0),
        velocity=Velocity(5.0, 3.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    player1 = Paddle(
        position=Position(10.0, 350.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )
    player2 = Paddle(
        position=Position(980.0, 350.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )
    score = Score()

    result = update_game.execute(ball, player1, player2, score, 0.016)
    # Ball should move
    assert ball.position.x != 500.0 or ball.position.y != 400.0
    # No score yet
    assert result is None


def test_handle_input_execute():
    """Test handle input use case."""
    mock_input_handler = Mock()
    mock_input_handler.should_quit.return_value = False
    mock_input_handler.is_key_pressed.return_value = False
    mock_input_handler.get_events.return_value = []

    handle_input = HandleInput(mock_input_handler, 800.0)

    player2 = Paddle(
        position=Position(980.0, 350.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )

    actions = handle_input.execute(player2, 0.016)
    assert actions["quit"] is False
    assert actions["pause"] is False

