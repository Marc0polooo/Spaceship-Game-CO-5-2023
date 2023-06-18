from game.components.powers.power import Power
from game.utils.constants import HEAVY_MACHINE_GUN,HEAVY_TYPE

class HeavyMachineGun(Power):
    def __init__(self)  :
        super().__init__(HEAVY_MACHINE_GUN,HEAVY_TYPE)