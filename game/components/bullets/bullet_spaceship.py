import pygame
from game.components.bullets.bullet import Bullet

from game.utils.constants import BULLET,BULLET_TYPE,DOBLE_BULLET,HEAVY_TYPE


class MyBullet(Bullet):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20

    def __init__(self, center): #se que no se debe hacer pero no encuentro otra manera de actualizar la imagen y los valores
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.type = BULLET_TYPE
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_active = True

    def update(self,enemy):
        self.rect.y -= self.SPEED
        #if player.power_type == HEAVY_TYPE:
        #     WIDTH = 30
        #     HEIGTH = 34
        #     self.image = DOBLE_BULLET
        #     self.image = pygame.transform.scale(self.image, (WIDTH, HEIGTH))
            
        if self.rect.y <= 0:
            self.is_active = False
        super().update(enemy)

        if not self.is_active:
            enemy.is_destroyed = True

    def power_up(self):
        self.image = DOBLE_BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        