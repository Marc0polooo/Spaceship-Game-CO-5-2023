import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY,BULLET_ENEMY_TYPE,SCREEN_HEIGHT,SHIELD_TYPE


class BulletEnemy(Bullet):

    width = 9
    heigth = 32
    speed = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image,(self.width, self.heigth))
        self.type = BULLET_ENEMY_TYPE
        super().__init__(self.image,self.type,center)

    def update(self, player):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_active = False
        elif self.rect.colliderect(player.rect) and player.power_type == SHIELD_TYPE :
             self.is_active = False
        elif not player.power_type == SHIELD_TYPE:
            super().update(player)

    
