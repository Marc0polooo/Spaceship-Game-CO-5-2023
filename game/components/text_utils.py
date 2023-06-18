from pygame.font import Font
from game.utils.constants import FONT_STYLE,SCREEN_WIDTH,SCREEN_HEIGHT,BUTTON_PLAY
import pygame

def get_message(message,size,color,width = SCREEN_WIDTH //2 ,height = SCREEN_HEIGHT // 2):
    font = Font(FONT_STYLE,size)
    text = font.render(message,True,color)
    text_rect = text.get_rect()
    text_rect.center = (width,height)
    
    return text,text_rect
    

def get_image(image,width = SCREEN_WIDTH //2 ,height = SCREEN_HEIGHT // 2):
    play = image
    play  = pygame.transform.scale(play,(150,50))
    rect = play.get_rect()
    rect.center = (width,height)
    return play, rect
