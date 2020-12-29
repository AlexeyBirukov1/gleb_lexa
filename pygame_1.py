import time
import pygame

from d import Ui_MainWindow
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
sprite2 = pygame.sprite.Sprite()

sprite.image = pygame.image.load('sp/paddle_big.png')
sprite2.image = pygame.image.load('sp/ball.png')

sprite.rect = sprite.image.get_rect()
sprite2.rect = sprite2.image.get_rect()

all_sprites.add(sprite)
all_sprites2.add(sprite2)


bg = pygame.image.load("sp/backgroung.png")
bg2 = [pygame.image.load("sp/menu.png"), pygame.image.load("sp/menu_2.png") , pygame.image.load("sp/menu_3.png"),
       pygame.image.load("sp/menu_2.png")]
bg3 = [pygame.image.load("sp/screen_1.png"), pygame.image.load("sp/screen_2.png"), pygame.image.load("sp/screen_3.png")]

def menu():
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('ШАРЫ')
        screen = pygame.display.set_mode((600, 600))
        running = True
        clock = pygame.time.Clock()
        fps = 100
        c = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
            c = c % 4
            screen.blit(bg2[c], (0, 0))
            time.sleep(0.5)
            c += 1
            clock.tick(fps)
            pygame.display.flip()
        main_1()


def main_1():
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('ШАРЫ')
        screen = pygame.display.set_mode((700, 525))
        running = True
        clock = pygame.time.Clock()
        fps = 100
        c = 0
        c1 = 0
        while running:
            if c1 > 2:
                running = False
            c = c % 3
            screen.blit(bg3[c], (0, 0))
            time.sleep(1)
            c += 1
            c1 += 1
            print(c1)
            clock.tick(fps)
            pygame.display.flip()
    main()

def main():
    circles = []
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('ШАРЫ')
        screen = pygame.display.set_mode((800, 600))
        circles.append(list((400, 300)))
        running = True
        clock = pygame.time.Clock()
        fps = 100
        sprite.rect.y = 520
        sprite.rect.x = 300
        sprite2.rect.y = 300
        sprite2.rect.x = 400

        dx = 2
        dy = 2

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            sprite2.rect.x += dx
            sprite2.rect.y += dy
            if sprite2.rect.y > 555:
                sprite2.rect.y = 300
                sprite2.rect.x = 400
            if sprite2.rect.y < 0:
                dy *= -1
            if sprite2.rect.x > 725 or sprite2.rect.x < 0:
                dx *= -1
            if sprite2.rect.x == sprite.rect.x and sprite2.rect.y == 550:
                dy *= -1
            if sprite.rect.x <= 0:
                sprite.rect.x = 1
            if sprite.rect.x >= 650:
                sprite.rect.x = 649

            # ------------------------------------------
            o = 1
            if key[pygame.K_RIGHT]:
                sprite.rect.x = sprite.rect.x + 2
            if key[pygame.K_LEFT]:
                sprite.rect.x = sprite.rect.x - 2
            if pygame.sprite.collide_mask(sprite, sprite2):
                dy *= -1
                dx *= 1
            screen.blit(bg, (0, 0))
            try:
                all_sprites.draw(screen)
                all_sprites2.draw(screen)
            except Exception as e:
                print(e)
            clock.tick(fps)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    menu()