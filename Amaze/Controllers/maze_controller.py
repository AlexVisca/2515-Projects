#from player import Player
from pygame.locals import *
import pygame
from mazegame import Maze
from mazegame import Player
from mazegame import App

class MazeController:
    def __init__(self):
        self.Maze = Maze()
        self.Player = Player()
        self.App = App()
    
    def on_execute(self):
        if self.App.on_init() == False:
            self.App._running = False
 
        while( self.App._running ):
            
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[ord('a')]):
                self.Player.moveRight()
 
            if (keys[ord('d')]):
                self.Player.moveLeft()
 
            if (keys[ord('w')]):
                self.Player.moveUp()
 
            if (keys[ord('s')]):
                self.Player.moveDown()
 
            if (keys[K_ESCAPE]):
                self.App._running = False
 
            self.App.on_loop()
            self.App.on_render()
        self.App.on_cleanup()
  
if __name__ == '__main__':
    theApp = MazeController()
    theApp.on_execute()
  



