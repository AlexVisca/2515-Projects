from player import Player
from pygame.locals import *
import pygame
from maze import Maze


class MazeController:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
        self.view = View(self)
  
    def on_execute(self):
        if self.view.on_init() == False:
            self._running = False
 
        while( self._running ):
            
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[ord('a')]):
                self.player.moveRight()
 
            if (keys[ord('d')]):
                self.player.moveLeft()
 
            if (keys[ord('w')]):
                self.player.moveUp()
 
            if (keys[ord('s')]):
                self.player.moveDown()
 
            if (keys[ord('q')]):
                self._running = False
            
 
            self.view.on_render()
        self.view.on_cleanup()
  
if __name__ == '__main__':
    theApp = MazeController()
    theApp.on_execute()
  




