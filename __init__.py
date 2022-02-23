class Gun:
    magazine_size = 0

    def __init__(self):
        self.loaded_bullets = self.magazine_size

    def shoot(self):
        if self.loaded_bullets:
            self.loaded_bullets -= 1
            print(self.shoot_sound)
        else:
            print(self.no_bullets_sound)

    def reload(self):
        self.magazine_loaded = self.magazine_size
        print(self.reload_sound)


class Sprayable:
    def spray_shoot(self, times=1):
        if self.loaded_bullets:

            if times > self.loaded_bullets:
                available_times = self.loaded_bullets
            else:
                available_times = times

            self.loaded_bullets -= available_times
            print(f"{self.shoot_sound} " * available_times)
        else:
            print(self.no_bullets_sound)


class Silenceable:
    silence_shoot_sound = "Пиу."

    def __new__(cls, *args, **kwargs):
        cls = super().__new__(cls)
        cls.normal_shoot_sound = cls.shoot_sound
        return cls

    def attach_silencer(self):
        self.silencer = True
        self.shoot_sound = self.silence_shoot_sound

    def remove_silencer(self):
        self.silencer = False
        self.shoot_sound = self.normal_shoot_sound
