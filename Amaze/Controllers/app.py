import pygame
from pygame.locals import *
from MazeMVC.Models.maze import Maze
from MazeMVC.Models.player import Player


class App:
    """Main Application Controller"""
    __width = 800
    __height = 600
    # player = 0

    def __init__(self):
        self._running = True
        self._display = None
        self._image = None
        self._block = None
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.__width, self.__height), pygame.HWSURFACE)
        # Window caption
        pygame.display.set_caption('Amaze Game')
        self._running = True
        self._image = pygame.image.load("pygame.png").convert()
        self._block = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self._image, (self.player.x, self.player.y))
        self.maze.draw(self._display, self._block)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        """Keyboard Controller"""
        self.on_init()

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.move_right()

            if keys[K_LEFT]:
                self.player.move_left()

            if keys[K_UP]:
                self.player.move_up()

            if keys[K_DOWN]:
                self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

