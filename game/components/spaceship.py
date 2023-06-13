import pygame
from game.utils.constants import SPACESHIP,SCREEN_WIDTH
class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    def __init__(self):
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def update(self,user_input):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
            if self.rect.x == 0:
                self.rect.x = SCREEN_WIDTH
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
            if self.rect.x == 1060:
                self.rect.x = 0
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 10
    def move_down(self):
        if self.rect.y < 500:
            self.rect.y += 10