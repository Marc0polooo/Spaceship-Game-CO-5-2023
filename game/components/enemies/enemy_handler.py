
from game.components.enemies.ship import Ship
from game.components.enemies.enemy_two import EnemyTwo
from game.components.enemies.enemy_three import EnemyThree
from game.components.enemies.enemy import Enemy



class EnemyHandler:

    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.numer_boss = 1
        self.boss = False

    def update(self, bullet_handler):
        self.add_enemy()
        self.add_boss()
        self.boss_manager()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.number_enemy_destroyed += 1
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)


    def add_enemy(self):
        
            if len(self.enemies) < 2 and not self.boss:
                self.enemies.append(Ship())
                self.enemies.append(EnemyTwo())
            
    def add_boss(self):
        if self.number_enemy_destroyed == 2 and self.numer_boss == 1:
            self.numer_boss += 1
            self.enemies.append(EnemyThree())

    def boss_manager(self):
        for enemy in self.enemies:
            if  type(enemy) == EnemyThree:
                self.boss = True
            elif not type(enemy) == EnemyThree:
                self.boss = False

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.numer_boss = 1
        self.boss = False
        