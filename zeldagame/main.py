# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:14:16 2023

@author: Elizabeth

Zelda/darksouls like game
"""
import pygame, sys
# imports everything from settings
from settings import *
from level import Level
class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zeldalike')
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill('black')
            self.level.run()
            pygame.display.update() #uptdates the screen
            self.clock.tick(FPS)
            
if __name__ == '__main__':  #checks if main file
    game = Game()           #creates an instance of the game class
    game.run()              #calls the game class run function

