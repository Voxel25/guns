from guns import Silenceable
from guns.rifle import AssaultRifle


class AK47(AssaultRifle, Silenceable):
	magazine_size = 30

	silence_shoot_sound = "Ти."
