from pygame.locals import *
import pygame
from maze import Maze
from player import Player


class View:
    windowWidth = 800
    windowHeight = 600
    
    def __init__(self, controller):
        self.controller = controller
 
    def on_init(self):
       pygame.init()
       self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
       pygame.display.set_caption('maze game')
       self._running = True
       self._image_surf = pygame.image.load("pygame.png").convert()
       self._block_surf = pygame.image.load("pygame.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    
 


    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.controller.player.x,self.controller.player.y))
        self.controller.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()