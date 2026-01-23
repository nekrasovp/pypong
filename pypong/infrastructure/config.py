"""Game configuration."""

import os
from pathlib import Path

# Screen configuration
SCREEN_WIDTH = int(os.getenv("PYPONG_SCREEN_WIDTH", "1280"))
SCREEN_HEIGHT = int(os.getenv("PYPONG_SCREEN_HEIGHT", "960"))
FPS = int(os.getenv("PYPONG_FPS", "60"))

# Colors (RGB)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
WHITE = (255, 255, 255)

# Ball configuration
BALL_SIZE = 30.0
BALL_SPEED = 400.0  # Pixels per second

# Paddle configuration
PADDLE_WIDTH = 10.0
PADDLE_HEIGHT = 140.0
PADDLE_SPEED = 300.0  # Pixels per second
PADDLE_MARGIN = 10.0  # Distance from screen edge

# Asset paths
ASSETS_DIR = Path(__file__).parent.parent / "assets"
FONT_PATH = ASSETS_DIR / "8-BIT WONDER.TTF"
FONT_SIZE = 24

# Game timing
SCORE_RESET_DELAY_MS = 2100  # Milliseconds to wait before resetting ball after score
COUNTDOWN_3_MS = 700
COUNTDOWN_2_MS = 1400
COUNTDOWN_1_MS = 2100

