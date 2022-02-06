from abc import ABCMeta, abstractmethod

import pygame


class SceneBase(metaclass=ABCMeta):
    def __init__(self):
        self.next = self

    @abstractmethod
    def process_input(self, events, pressed_keys):
        """Input processing method
        :type pressed_keys: object
        :type events: object
        """

    @abstractmethod
    def update(self):
        """Update method"""

    @abstractmethod
    def render(self, screen):
        """Render method
        :type screen: object
        """

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(GameScene())

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255, 0, 0))


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self, screen: pygame):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))


run_game(400, 300, 60, TitleScene())
