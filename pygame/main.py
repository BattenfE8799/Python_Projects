# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:09:06 2023

@author: Eliza
"""
import pygame, sys 

class Item():
    def __init__(self, value, name, description):
        
        self.value = 0
        self.name = ''
        self.description = ''

class Player():
    def __init__(self):
        
        #general setup
        self.invintory = {}
        self.gold = 0
        self.weighttotal = 0
        self.weightcapacity = 150
        self.overweight = False
        self.health = 50
        self.healthtotal = 100
        self.stam = 50
        self.stamtotal = 100
        self.mana = 50
        self.manatotal = 100
        self.alive = True
        self.x = 0 
        self.y = 0
        self.z = 0
        
    def overweight_yn(self):
        if self.weighttotal >= self.weightcapacity:
            self.overweight = True
        else:
            self.overweight = False
            
    def add_to_weight(self, weight):
        weight = weight
        weight_num = self.weighttotal
        weighttotal = weight + weight_num
        self.weighttotal  = weighttotal
        self.overweight_yn()
        
    def add_item(self, item):
        self.invintory[item.name] = [item.description]
    
class Game():
    def main():
        #initializes the pygame module
        pygame.init()
        #load and set the logo
        logo = pygame.image.load('logo32x32.png')
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Game")
        image = pygame.image.load('image.png')
        
        # create a surface on screen that has the size
        screen = pygame.display.set_mode((600,600))
        screen.blit(image, (50,50))
        # define a variable to control the main loop
        running = True
        
        #main loop
        while running:
            pygame.display.flip()
            #event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    #change the value to False, to exit the main loop
                    running = False
    
    
if __name__ == '__main__':
    player = Player()
    player.overweight_yn()
    
    print(player.overweight)
    weight = 160
    player.add_to_weight(weight)
    print(player.overweight)
    print(player.weighttotal)
    key = Item(0,'key','a golden key.')
    player.add_item(key)
    print(player.invintory)
    game = Game
    game.main()
    