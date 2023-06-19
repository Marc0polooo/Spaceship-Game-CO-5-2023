from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_spaceship import MyBullet
from game.utils.constants import HEAVY_TYPE,DOBLE_BULLET

class BulletHandler:

    def __init__(self):

        self.bullets = []
        

    def update(self, player, enemies):
            
        for bullet in self.bullets:
            if not bullet.is_active:
                self.remove_bullet(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player,enemies)
                else:
                    for enemy in enemies:
                        bullet.update(player,enemy)


    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_TYPE:
            self.bullets.append(MyBullet(center))

    def remove_bullet(self,bullet):
        self.bullets.remove(bullet)
    
    def reset(self):
        self.bullets = []