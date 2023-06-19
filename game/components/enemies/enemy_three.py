import pygame,random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3,SCREEN_WIDTH,SCREEN_HEIGHT

class EnemyThree(Enemy):

    HEIGTH = 100
    WIDTH = 100
    SPEED_X = 8
    SPEED_Y = 5
    INTERVAL = 150
    SHOOTING_TIME = 5
    DOWN = "down"
    UP = "up"

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        
        self.move_boss = 300
        self.move_y = self.DOWN
        super().__init__(self.image)
        self.time = 0
        self.live = 20
        self.bullet_x = True

    def move(self):
        self.time += 1
        if  self.time >= self.move_boss  and self.move_y == self.DOWN :
            self.bullet_x = True
            self.rect.y += self.SPEED_Y
            
            if self.rect.y >= SCREEN_HEIGHT - self.HEIGTH:
                self.move_y = self.UP

        elif self.move_y == self.UP:
            self.rect.y -= self.SPEED_Y
            self.bullet_x = True
            if self.rect.y  <= 10:
                self.rect.y = self.rect.y
                self.bullet_x = False
                self.move_y =  self.DOWN
                self.time = 0

        if self.mov_x == self.LEFT and self.time < self.move_boss:
            self.rect.x -= self.SPEED_X
            if  self.rect.x <= 0:
                self.mov_x = self.RIGHT
                

        elif self.mov_x == self.RIGHT and self.time < self.move_boss:
            self.rect.x += self.SPEED_X
            if self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
       

    def leve_up_dificulty(self):
        pass

    def retec(self):
        self.live = 20