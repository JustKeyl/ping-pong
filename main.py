from pygame import *

back = [100, 150, 150]
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

class racket(sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = Surface((20, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
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

class racket_right(racket):
    def __init__(self, color):
        super().__init__(color)
        self.pos = (550, 250)
        self.rect.center = self.pos
        self.key_up = K_UP
        self.key_down = K_DOWN


player1 = racket("white")
player2 = racket_right("black")

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

    display.update()
    clock.tick(FPS)