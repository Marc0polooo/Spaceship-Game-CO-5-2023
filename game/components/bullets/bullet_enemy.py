import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY


class BulletEnemy(Bullet):

    width = 9
    heigth = 32
    spedd = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image,(self.width, self.heigth))
        super().__init__(self.image,center)

    def update(self, player):
        self.rect.y += self.spedd
        if self.rect.colliderect(player.rect):
            player.is_alive = False

    
