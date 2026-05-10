from pygame import *
from random import randint

back = [100, 150, 150]
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = Surface((20, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Racket(GameSprite):
    def __init__(self, color):
        super().__init__(color)
        self.pos = (50, 250)
        self.rect.center = self.pos
        self.key_up = K_w
        self.key_down = K_s
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        keys = key.get_pressed()
        if keys[self.key_up] and self.rect.y >= 20:
            self.rect.y -= 5
        elif keys[self.key_down] and self.rect.y <= 380:
            self.rect.y += 5

class Racket_right(Racket):
    def __init__(self, color):
        super().__init__(color)
        self.pos = (550, 250)
        self.rect.center = self.pos
        self.key_up = K_UP
        self.key_down = K_DOWN

class Ball(GameSprite):
    def __init__(self, color, speed):
        super().__init__(color)
        self.image = Surface((30, 30), SRCALPHA)
        draw.circle(self.image, color, (15, 15), 15)
        self.pos = (300, 250)
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.center = self.pos
        self.speed = speed

        self.speed_x = self.speed
        self.speed_y = self.speed

    def update(self):
        self.speed += 0.01
        self.speed_x += 0.01

        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1

        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.speed_y = self.speed
            self.speed_x *= -1
            self.speed_y *= -1 * (randint(1, 10) / 10)

        self.rect.x += 1 * self.speed_x
        self.rect.y += 1 * self.speed_y

        window.blit(self.image, (self.rect.x, self.rect.y))


player1 = Racket("white")
player2 = Racket_right("black")
ball1 = Ball("darkgrey", 5)

clock = time.Clock()
FPS = 30
game = True
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False


    player1.update()
    player2.update()
    ball1.update()

    display.update()
    clock.tick(FPS)