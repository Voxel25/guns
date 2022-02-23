from guns import Gun


class Shotgun(Gun):
    shoot_sound = "Пау. Чик-чик."
    reload_sound = "Чик-чик."
    load_bullet_sound = "Чик."
    no_bullets_sound = "Чик."

    def reload(self):
        self.magazine_loaded = self.magazine_size
        free_space = self.magazine_size - self.loaded_bullets
        print(f"{self.load_bullet_sound} " * free_space + self.reload_sound)
