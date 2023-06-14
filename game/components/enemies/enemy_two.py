import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Ship_two(Enemy):
    WIDTH = 40
    HEIGTH = 60
    
    
    def __init__(self):
        self.image = self.Enemi()
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        super().__init__(self.image)

    def Enemi(self):
        self.SPEED_X = 6
        self.SPEED_Y = 5
        return ENEMY_2
