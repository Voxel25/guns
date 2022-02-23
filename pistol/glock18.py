from guns import Sprayable, Silenceable
from guns.pistol import Pistol

class Glock18(Pistol, Sprayable, Silenceable):
	magazine_size = 20
