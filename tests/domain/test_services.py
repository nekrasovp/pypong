"""Tests for domain services."""

from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.services.ball_physics import BallPhysics
from pypong.domain.services.collision_detector import CollisionDetector
from pypong.domain.services.score_manager import ScoreManager
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


def test_collision_detector_ball_paddle():
    """Test ball-paddle collision detection."""
    ball = Ball(
        position=Position(50.0, 50.0),
        velocity=Velocity(5.0, 0.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    paddle = Paddle(
        position=Position(40.0, 40.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )

    assert CollisionDetector.ball_paddle_collision(ball, paddle) is True


def test_collision_detector_no_collision():
    """Test collision detection when no collision."""
    ball = Ball(
        position=Position(100.0, 100.0),
        velocity=Velocity(5.0, 0.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    paddle = Paddle(
        position=Position(10.0, 10.0),
        dimensions=Dimensions(10.0, 140.0),
        speed=7.0,
    )

    assert CollisionDetector.ball_paddle_collision(ball, paddle) is False


def test_ball_physics_update_position():
    """Test ball physics position update."""
    ball = Ball(
        position=Position(0.0, 0.0),
        velocity=Velocity(5.0, 3.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    BallPhysics.update_ball_position(ball, 1.0)
    assert ball.position.x == 5.0
    assert ball.position.y == 3.0


def test_ball_physics_wall_collision():
    """Test ball physics wall collision."""
    ball = Ball(
        position=Position(50.0, 0.0),
        velocity=Velocity(5.0, -5.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    BallPhysics.handle_wall_collision(ball, 1000.0, 1000.0)
    # Should reverse y velocity when hitting top wall
    assert ball.velocity.y == 5.0


def test_score_manager_check_out_of_bounds():
    """Test score manager out of bounds check."""
    ball = Ball(
        position=Position(-10.0, 100.0),
        velocity=Velocity(-5.0, 0.0),
        dimensions=Dimensions(30.0, 30.0),
    )
    scorer = ScoreManager.check_ball_out_of_bounds(ball, 1000.0)
    assert scorer == "player2"


def test_score_manager_update_score():
    """Test score manager update score."""
    score = Score()
    ScoreManager.update_score(score, "player1")
    assert score.player1 == 1
    assert score.player2 == 0

    ScoreManager.update_score(score, "player2")
    assert score.player1 == 1
    assert score.player2 == 1

