import random
import pygame


class Button():
    def __init__(self, x, y, pos, width, heigth,):
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
        self.pos = pos
        
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
        
class RpsGame():
    def__init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(960, 640)
        pygame.display.set_caption("RPS smasher")
        
        self.bg = pygame.image.load(background.jpg)
        self.r_