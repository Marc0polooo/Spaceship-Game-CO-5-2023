from game.components.powers.shield import Shield
from game.components.powers.heavy_machine_gun import HeavyMachineGun
import random,pygame
from game.utils.constants import SPACESHIP_SHIELD,SCREEN_HEIGHT, SHIELD_TYPE

class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appers = random.randint(3000,7000)
        self.duration = random.randint(1,6)
        self.random_power = random.randint(1,2)

    def generate_power(self):
        if self.random_power == 1:
            power = Shield()
        else:
            power = HeavyMachineGun()
        self.powers.append(power)
        self.when_appers += random.randint(3000,7000)


    def update(self,player):
        self.duration = random.randint(1,2)
        self.random_power = random.randint(1,2)
        current_tipe = pygame.time.get_ticks()
        if len(self.powers) == 0 and current_tipe >= self.when_appers:
            self.generate_power()
        self.power_use(player)
        
    
    def draw(self,screen):
        for power in self.powers:
            power.draw(screen)

    def delete_power_image(self,power,player):
        if power.rect.y >= SCREEN_HEIGHT or power.rect.colliderect(player.rect):
            power = self.powers.remove(power)
            


    def power_use(self,player):
        for power in self.powers:
            power.update()
            self.delete_power_image(power,player)
            if player.rect.colliderect(power.rect):
                power.star_time = pygame.time.get_ticks()
                player.power_type = power.type  
                player.has_power = True
                player.power_time = power.star_time + (self.duration * 1000)
                if player.power_type ==  SHIELD_TYPE:
                    player.set_power_image(SPACESHIP_SHIELD)

    def reset(self):
        self.powers = []
        self.duration = random.randint(1,6)