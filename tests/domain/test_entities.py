"""Tests for domain entities."""

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


def test_ball_move():
    """Test ball movement."""
    ball = Ball(
        position=Position(0.0, 0.0),
        velocity=Velocity(5.0, 3.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    ball.move(1.0)
    assert ball.position.x == 5.0
    assert ball.position.y == 3.0


def test_ball_reverse_x_velocity():
    """Test ball x velocity reversal."""
    ball = Ball(
        position=Position(0.0, 0.0),
        velocity=Velocity(5.0, 3.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    ball.reverse_x_velocity()
    assert ball.velocity.x == -5.0
    assert ball.velocity.y == 3.0


def test_paddle_move_up():
    """Test paddle movement up."""
    paddle = Paddle(
        position=Position(10.0, 100.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )
    paddle.move_up(1.0)
    assert paddle.position.y == 93.0


def test_paddle_move_down():
    """Test paddle movement down."""
    paddle = Paddle(
        position=Position(10.0, 100.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )
    paddle.move_down(1.0, max_y=1000.0)
    assert paddle.position.y == 107.0


def test_score_increment():
    """Test score increment."""
    score = Score()
    assert score.player1 == 0
    assert score.player2 == 0

    score.increment_player1()
    assert score.player1 == 1
    assert score.player2 == 0

    score.increment_player2()
    assert score.player1 == 1
    assert score.player2 == 1


def test_score_reset():
    """Test score reset."""
    score = Score()
    score.increment_player1()
    score.increment_player2()
    score.reset()
    assert score.player1 == 0
    assert score.player2 == 0

