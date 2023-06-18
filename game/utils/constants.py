import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

HEAVY_MACHINE_GUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/H.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

BUTTON_PLAY = pygame.image.load(os.path.join(IMG_DIR, 'Other/boton_trans.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEAVY_TYPE = "heavy"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
DOBLE_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/doble_bullet.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/file.jpg"))

BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)
GOLD_COLOR = (212, 175, 55)

FONT_STYLE = 'freesansbold.ttf'
BULLET_ENEMY_TYPE = 'enemy'
BULLET_TYPE = 'player'
