from guns import Silenceable
from guns.rifle import AssaultRifle


class M4(AssaultRifle, Silenceable):
    magazine_size = 30

    silence_shoot_sound = "Ту."
