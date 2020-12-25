from random import randint
import pygame as pg
import sys

W = 400
H = 400
WHITE = (255, 255, 255)


class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x, 0))


sc = pg.display.set_mode((W, H))

# координата x будет случайна
car1 = Car(randint(1, W), 'car1.png')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pg.display.update()
    pg.time.delay(20)

    # машинка ездит сверху вниз
    if car1.rect.y < H:
        car1.rect.y += 2
    else:
        car1.rect.y = 0


class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x, 0))

    def update(self):
        if self.rect.y < H:
            self.rect.y += 2
        else:
            self.rect.y = 0


sc = pg.display.set_mode((W, H))

# координата x будет случайна
car1 = Car(randint(1, W), 'car1.png')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pg.display.update()
    pg.time.delay(20)

    car1.update()
car1 = Car(randint(1, W), 'car1.png')
car2 = Car(randint(1, W), 'car2.png')
car3 = Car(randint(1, W), 'car3.png')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    sc.blit(car2.image, car2.rect)
    sc.blit(car3.image, car3.rect)
    pg.display.update()
    pg.time.delay(20)

    car1.update()
    car2.update()
    car3.update()