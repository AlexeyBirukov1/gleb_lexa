import os
import sys
import time
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('sp', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
tile_images = {
    'r': load_image('block_red.png'),
    'R': load_image('block_red_sealed.png'),
}
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
sprite2 = pygame.sprite.Sprite()
sprite1_1 = pygame.sprite.Sprite()
sprite1_2 = pygame.sprite.Sprite()
sprite1_3 = pygame.sprite.Sprite()
sprite1_4 = pygame.sprite.Sprite()
sprite1_5 = pygame.sprite.Sprite()
sprite2_1 = pygame.sprite.Sprite()
sprite2_2 = pygame.sprite.Sprite()
sprite2_3 = pygame.sprite.Sprite()
sprite2_4 = pygame.sprite.Sprite()
sprite2_5 = pygame.sprite.Sprite()

sprite1_1.image = pygame.image.load('sp/block_red.png')
sprite1_1.rect = sprite1_1.image.get_rect()

sprite1_2.image = pygame.image.load('sp/block_red_sealed.png')
sprite1_2.rect = sprite1_2.image.get_rect()

sprite1_3.image = pygame.image.load('sp/block_red.png')
sprite1_3.rect = sprite1_3.image.get_rect()

sprite1_4.image = pygame.image.load('sp/block_red_sealed.png')
sprite1_4.rect = sprite1_4.image.get_rect()

sprite1_5.image = pygame.image.load('sp/block_red_sealed.png')
sprite1_5.rect = sprite1_5.image.get_rect()

sprite2_1.image = pygame.image.load('sp/block_red.png')
sprite2_1.rect = sprite1_1.image.get_rect()
sprite2_2.image = pygame.image.load('sp/block_red_sealed.png')
sprite2_2.rect = sprite1_2.image.get_rect()
sprite2_3.image = pygame.image.load('sp/block_red.png')
sprite2_3.rect = sprite1_3.image.get_rect()
sprite2_4.image = pygame.image.load('sp/block_red_sealed.png')
sprite2_4.rect = sprite1_4.image.get_rect()
sprite2_5.image = pygame.image.load('sp/block_red_sealed.png')
sprite2_5.rect = sprite1_5.image.get_rect()

all_sprites3.add(sprite1_1)
all_sprites3.add(sprite1_2)
all_sprites3.add(sprite1_3)
all_sprites3.add(sprite1_4)
all_sprites3.add(sprite1_5)
all_sprites3.add(sprite2_1)
all_sprites3.add(sprite2_2)
all_sprites3.add(sprite2_3)
all_sprites3.add(sprite2_4)
all_sprites3.add(sprite2_5)

sprite.image = pygame.image.load('sp/paddle_big.png')
sprite2.image = pygame.image.load('sp/ball.png')

sprite.rect = sprite.image.get_rect()
sprite2.rect = sprite2.image.get_rect()

all_sprites.add(sprite)
all_sprites2.add(sprite2)
tile_height = 78
tile_width = 160

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
    # player, level_x, level_y = generate_level(write_map('sp/map.txt'))
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
        x_block = 0
        x_block1 = 0
        y_block = 80
        sprite.rect.y = 520
        sprite.rect.x = 300
        sprite2.rect.y = 300
        sprite2.rect.x = 400

        sprite2_1.rect.y = y_block
        sprite2_2.rect.y = y_block
        sprite2_3.rect.y = y_block
        sprite2_4.rect.y = y_block
        sprite2_5.rect.y = y_block

        sprite1_1.rect.y = 0
        sprite1_2.rect.y = 0
        sprite1_3.rect.y = 0
        sprite1_4.rect.y = 0
        sprite1_5.rect.y = 0

        sprite2_1.rect.x = x_block1
        x_block1 += 160
        sprite2_2.rect.x = x_block1
        x_block1 += 160
        sprite2_3.rect.x = x_block1
        x_block1 += 160
        sprite2_4.rect.x = x_block1
        x_block1 += 160
        sprite2_5.rect.x = x_block1

        sprite1_1.rect.x = x_block
        x_block += 160
        sprite1_2.rect.x = x_block
        x_block += 160
        sprite1_3.rect.x = x_block
        x_block += 160
        sprite1_4.rect.x = x_block
        x_block += 160
        sprite1_5.rect.x = x_block

        dx = 3
        dy = 2
        block = []
        # write_map('sp/map.txt')
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            sprite2.rect.x += dx
            sprite2.rect.y += dy
            if sprite2.rect.y > 555:
                running = False
                main_2()
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
                sprite.rect.x = sprite.rect.x + 3
            if key[pygame.K_LEFT]:
                sprite.rect.x = sprite.rect.x - 3
            if pygame.sprite.collide_mask(sprite, sprite2):
                dy *= -1
                dx *= 1
            if pygame.sprite.groupcollide(all_sprites2, all_sprites3, False, True):
                dy *= -1
                dx *= 1
                print(len(block))
                block.append(True)
                if len(block) == 8:
                    running = False
            screen.blit(bg, (0, 0))
            try:
                all_sprites.draw(screen)
                all_sprites2.draw(screen)
                all_sprites3.draw(screen)
            except Exception as e:
                print(e)
            clock.tick(fps)
            pygame.display.flip()
        pygame.quit()

def main_2():
    size = 600, 300
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load('sp/gameover.png')
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    all_sprites.add(sprite)
    clock = pygame.time.Clock()
    running = True
    fps = 100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("blue"))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    menu()

