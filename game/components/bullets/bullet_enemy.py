import pygame,random
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY,BULLET_ENEMY_TYPE,SCREEN_HEIGHT,SHIELD_TYPE
from game.components.enemies.enemy_three import EnemyThree
from game.utils.constants import BULLET_1,BULLET_0

class BulletEnemy(Bullet):

    width = 9
    heigth = 32
    speed = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image,(self.width, self.heigth))
        self.image_bullet1 = pygame.transform.scale(BULLET_1, (20, 40))
        self.image_bullet0 = pygame.transform.scale(BULLET_0, (20, 40))
        self.type = BULLET_ENEMY_TYPE
        super().__init__(self.image,self.type,center)

    def binarios(self,enemies):
        ran = random.randint(1,2)
        for enemy in enemies:
          
          if type(enemy) == EnemyThree: #isinstance(enemy, EnemyThree):
               if ran == 1:
                self.image = self.image_bullet1
                
               else:
                   self.image = self.image_bullet0

    def update(self, player,enemies):
        self.binarios(enemies)
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_active = False
        elif self.rect.colliderect(player.rect) and player.power_type == SHIELD_TYPE :
             self.is_active = False
        elif not player.power_type == SHIELD_TYPE:
            super().update(player)

    
