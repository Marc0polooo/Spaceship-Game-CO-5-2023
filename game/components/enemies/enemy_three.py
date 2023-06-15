import pygame,random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3,SCREEN_WIDTH

class EnemyThree(Enemy):

    HEIGTH = 60
    WIDTH = 60
    SPEED_X = 8
    SPEED_Y = 2   
    

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        super().__init__(self.image) 