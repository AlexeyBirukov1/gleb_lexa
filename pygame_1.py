import os
import sys
import time
import pygame

lvls = ['sp/map.txt', 'sp/map2.txt', 'sp/map3.txt', 'sp/map4.txt', 'sp/map5.txt']
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
all_sprites4 = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
sprite2 = pygame.sprite.Sprite()

sprite.image = pygame.image.load('sp/paddle_big.png')
sprite2.image = pygame.image.load('sp/ball.png')

sprite.rect = sprite.image.get_rect()
sprite2.rect = sprite2.image.get_rect()
c_score = 0
all_sprites.add(sprite)
all_sprites2.add(sprite2)
tile_height = 78
lvl = 0
tile_width = 160


bg = pygame.image.load("sp/backgroung.png")
bg2 = []
for i in range(42):
    bg2.append(pygame.image.load("anim/tmp-" + str(i) + ".gif"))
bg3 = [pygame.image.load("sp/screen_1.png"), pygame.image.load("sp/screen_2.png"), pygame.image.load("sp/screen_3.png")]

class Block(pygame.sprite.Sprite):
    def __init__(self, color, sealed, pos_x, pos_y):
        self.color = color
        self.sealed = sealed
        super().__init__(all_sprites)
        self.image = tile_images[color]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if color == 'r':
            self.add(all_sprites3)
        else:
            self.add(all_sprites4)

def write_map(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'r' or level[y][x] == 'R':
                Block(level[y][x], False, x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

def menu():
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('ШАРЫ')
        screen = pygame.display.set_mode((960, 560))
        running = True
        clock = pygame.time.Clock()
        fps = 25
        c = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    running = False
            c = c % 41
            screen.blit(bg2[c], (0, 0))
            c += 1
            clock.tick(fps)
            pygame.display.flip()
        main(lvls[lvl])



def main(mapp='sp/map.txt'):
    circles = []
    if __name__ == '__main__':
        c_score = 0
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
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(c_score), False, (255, 255, 255))
        dx = 5
        dy = 5
        block = []
        player, level_x, level_y = generate_level(write_map(mapp))
        maxscore = len(all_sprites3)
        score = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            sprite2.rect.x += dx
            sprite2.rect.y += dy
            if sprite2.rect.y > 555:
                dy *= -1
                # running = False
                # main_2()
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
            if key[pygame.K_RIGHT]:
                sprite.rect.x = sprite.rect.x + 4
            if key[pygame.K_LEFT]:
                sprite.rect.x = sprite.rect.x - 4
            if pygame.sprite.collide_mask(sprite, sprite2):
                dy *= -1
                dx *= 1
            if pygame.sprite.groupcollide(all_sprites2, all_sprites3, False, True):
                if sprite2.rect.y == 76 or sprite2.rect.y == 154 or sprite2.rect.y == 232:
                    dy *= -1
                    dx *= 1
                else:
                    dy *= 1
                    dx *= -1
                score1 = score
                score = maxscore - len(all_sprites3)
                c_score += (score - score1) * 100
                textsurface = myfont.render(str(c_score), False, (255, 255, 255))
                if score == maxscore:
                    running = False
                    win()
            screen.blit(bg, (0, 0))
            try:
                all_sprites.draw(screen)
                all_sprites2.draw(screen)
                all_sprites3.draw(screen)
            except Exception as e:
                print(e)
            clock.tick(fps)
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()


def win(lvl1=lvl):
    global lvl
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load('sp/win.png')
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
            if event.type == pygame.KEYDOWN:
                running = False
        screen.fill(pygame.Color("blue"))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    if lvl < 4:
        lvl += 1
        main(lvls[lvl])



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


if __name__ == "__main__":
    menu()