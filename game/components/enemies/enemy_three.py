import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class EnemyThree(Enemy):

    HEIGTH = 100
    WIDTH = 100
    SPEED_X = 8
    SPEED_Y = 0
    INTERVAL = 150
    SHOOTING_TIME = 5   
    

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        super().__init__(self.image) 
    
    def move_boss(self):
        pass