import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class Ship_three(Enemy):
    WIDTH = 40
    HEIGTH = 60
    
    
    def __init__(self):
        self.image = self.Enemi()
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        super().__init__(self.image)

    def Enemi(self):
        self.WIDTH = 60
        self.SPEED_X = 20
        self.SPEED_Y = 1
        return ENEMY_3
