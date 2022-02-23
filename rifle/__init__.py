from guns import Gun, Sprayable


class Rifle(Gun):
    shoot_sound = "Та."
    reload_sound = "Вжук. Вжук. Чик-чик."
    no_bullets_sound = "Чик."


class AssaultRifle(Rifle, Sprayable):
	pass


class SniperRifle(Rifle):
    shoot_sound = "Пах. Чик-чик."
