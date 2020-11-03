# === Player === #


class Player:
    x = 44
    y = 44
    speed = 1

    def move_right(self):
        self.x = self.x + self.speed

    def move_left(self):
        self.x = self.x - self.speed

    def move_up(self):
        self.y = self.y - self.speed

    def move_down(self):
        self.y = self.y + self.speed
