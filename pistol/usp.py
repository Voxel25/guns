from guns import Silenceable
from guns.pistol import Pistol

class USP(Pistol, Silenceable):
	magazine_size = 12
