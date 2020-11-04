# === Player === #


class Player:
    x = 44
    y = 44
    speed = 1

    def moveRight(self):
        self.x = self.x - self.speed

    def moveLeft(self):
        self.x = self.x + self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
