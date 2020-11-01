#from player import Player
from pygame.locals import *
import pygame
from mazegame import Maze
from mazegame import Player
from mazegame import App

class MazeController:
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
        
 
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
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
  
    
    def on_execute(self):
        if self.on_init() == False:
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
            
 
            self.on_render()
        self.on_cleanup()
  
if __name__ == '__main__':
    theApp = MazeController()
    theApp.on_execute()


