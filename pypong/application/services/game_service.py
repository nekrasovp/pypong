"""Game service for orchestrating game logic."""

from __future__ import annotations

import time

from pypong.application.interfaces.input_handler import InputHandler
from pypong.application.interfaces.renderer import Renderer
from pypong.application.use_cases.handle_input import HandleInput
from pypong.application.use_cases.update_game import UpdateGame
from pypong.domain.entities.ball import Ball
from pypong.domain.entities.paddle import Paddle
from pypong.domain.entities.score import Score
from pypong.domain.value_objects.color import BLACK, GREY
from pypong.domain.value_objects.dimensions import Dimensions
from pypong.domain.value_objects.position import Position
from pypong.domain.value_objects.velocity import Velocity


class GameService:
    """Service for orchestrating game logic."""

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
        screen_width: float,
        screen_height: float,
        ball_speed: float,
        paddle_speed: float,
    ) -> None:
        """Initialize game service.

        Args:
            renderer: Renderer interface
            input_handler: Input handler interface
            screen_width: Screen width
            screen_height: Screen height
            ball_speed: Ball speed magnitude
            paddle_speed: Paddle speed magnitude
        """
        self.renderer = renderer
        self.input_handler = input_handler
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball_speed = ball_speed
        self.paddle_speed = paddle_speed

        # Initialize game entities
        self.ball = self._create_ball()
        self.player1 = self._create_player1()
        self.player2 = self._create_player2()
        self.score = Score()

        # Initialize use cases
        self.update_game = UpdateGame(screen_width, screen_height, ball_speed)
        self.handle_input = HandleInput(input_handler, screen_height)

        # Game state
        self.score_time: float | None = None
        self.ball_moving = False

    def _create_ball(self) -> Ball:
        """Create ball entity."""
        import random

        from pypong.domain.value_objects.dimensions import Dimensions

        ball_size = 30.0
        center_x = self.screen_width / 2 - ball_size / 2
        center_y = self.screen_height / 2 - ball_size / 2

        # Start with random velocity
        velocity_x = self.ball_speed * random.choice((1, -1))
        velocity_y = self.ball_speed * random.choice((1, -1))

        return Ball(
            position=Position(center_x, center_y),
            velocity=Velocity(velocity_x, velocity_y),
            dimensions=Dimensions(ball_size, ball_size),
        )

    def _create_player1(self) -> Paddle:
        """Create player 1 paddle (AI)."""
        from pypong.domain.value_objects.dimensions import Dimensions

        paddle_width = 10.0
        paddle_height = 140.0
        paddle_x = 10.0
        paddle_y = self.screen_height / 2 - paddle_height / 2

        return Paddle(
            position=Position(paddle_x, paddle_y),
            dimensions=Dimensions(paddle_width, paddle_height),
            speed=self.paddle_speed,
        )

    def _create_player2(self) -> Paddle:
        """Create player 2 paddle (human)."""
        from pypong.domain.value_objects.dimensions import Dimensions

        paddle_width = 10.0
        paddle_height = 140.0
        paddle_x = self.screen_width - 20.0
        paddle_y = self.screen_height / 2 - paddle_height / 2

        return Paddle(
            position=Position(paddle_x, paddle_y),
            dimensions=Dimensions(paddle_width, paddle_height),
            speed=self.paddle_speed,
        )

    def update(self, delta_time: float) -> dict[str, bool]:
        """Update game state.

        Args:
            delta_time: Time elapsed since last update

        Returns:
            Dictionary with game state flags
        """
        # Handle input
        input_actions = self.handle_input.execute(self.player2, delta_time)

        # Update AI (player 1)
        self._update_ai(delta_time)

        # Update game
        result = self.update_game.execute(
            self.ball,
            self.player1,
            self.player2,
            self.score,
            delta_time,
        )

        # Handle scoring reset timer
        if result and "scored" in result:
            self.score_time = time.time()

        return input_actions

    def _update_ai(self, delta_time: float) -> None:
        """Update AI player (player 1)."""
        # Simple AI: follow the ball
        target_y = self.ball.position.y
        self.player1.move_to_y(target_y, max_y=self.screen_height)

    def render(self) -> None:
        """Render the game."""
        # Clear screen
        self.renderer.clear(BLACK)

        # Draw center line
        center_x = self.screen_width / 2
        self.renderer.draw_line(
            Position(center_x, 0),
            Position(center_x, self.screen_height),
            GREY,
        )

        # Draw paddles
        self.renderer.draw_rect(self.player1.position, self.player1.dimensions, GREY)
        self.renderer.draw_rect(self.player2.position, self.player2.dimensions, GREY)

        # Draw ball
        ball_center = Position(
            self.ball.position.x + self.ball.dimensions.width / 2,
            self.ball.position.y + self.ball.dimensions.height / 2,
        )
        self.renderer.draw_circle(ball_center, self.ball.dimensions.width / 2, GREY)

        # Draw scores
        score_pos1 = Position(self.screen_width / 2 + 30, self.screen_height / 2 - 10)
        score_pos2 = Position(self.screen_width / 2 - 50, self.screen_height / 2 - 10)
        self.renderer.draw_text(str(self.score.player1), score_pos1, 24, GREY)
        self.renderer.draw_text(str(self.score.player2), score_pos2, 24, GREY)

        # Present frame
        self.renderer.present()

