from game.components.powers.power import Power
from game.utils.constants import HEART_TYPE, HEART

class PowerHeart(Power):
    def __init__(self):
        super().__init__(HEART,HEART_TYPE)