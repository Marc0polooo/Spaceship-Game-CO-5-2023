import pygame,random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1,ENEMY_2

class Ship(Enemy):
    WIDTH = 40
    HEIGTH = 60
    R = random.randint(1,2)
    

    def __init__(self):
        self.image = self.enemi_()
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        super().__init__(self.image)

    def enemi_(self):
        if self.R == 1:
            ENEMY_1
            return ENEMY_1
        else:
            ENEMY_2
            self.WIDTH = 30
            self.SPEED_X = 10
            self.SPEED_Y = 2
            self.INTERVAL = 50
            return ENEMY_2
