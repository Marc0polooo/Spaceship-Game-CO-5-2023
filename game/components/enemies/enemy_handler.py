
from game.components.enemies.ship import Ship
from game.components.enemies.enemy_two import Ship_two
from game.components.enemies.enemy_three import Ship_three
class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Ship_two())
        self.enemies.append(Ship_three())


    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)