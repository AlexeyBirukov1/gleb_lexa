import os
import sys
import pygame
from os import path
# Добро пожаловать в наш проект! Комментарии помогут вам разобраться с кодом
# Данная зона кода является подготовительной. Тут определяются главные переменные и функции

def load_image(name):
    fullname = os.path.join('sp', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
# Тут загружаются главные словари с путями к файлам, которые находятся в папке sp
# Массив lvls содержит пути к файлами, где прописаны уровни
# Словарь tile_images содержит имена текстур для блоков, которые будет выбивать шарик
lvls = ['sp/map.txt', 'sp/map2.txt', 'sp/map3.txt', 'sp/map4.txt', 'sp/map5.txt']
tile_images = {
    'r': load_image('block_red.png'),
    'R': load_image('block_red_sealed.png'),
}
# тут находятся группы спрайтов. all_sprites - это группа для ракетки,
# all_sprites2 - это группа для мячика,
# all_sprites3 - это группа для обычных блоков,
# all_sprites4 - это группа для блоков с усилениями
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()
all_sprites4 = pygame.sprite.Group()

sprite = pygame.sprite.Sprite() # это ракетка
sprite2 = pygame.sprite.Sprite() # это мячик

sprite.image = pygame.image.load('sp/paddle_big.png') # это картинка ракетки
sprite2.image = pygame.image.load('sp/ball.png') # это картинка мячика

sprite.rect = sprite.image.get_rect()
sprite2.rect = sprite2.image.get_rect()
# тут идет определение основных параметров
c_score = 0
all_sprites.add(sprite)
all_sprites2.add(sprite2)
tile_height = 78
lvl = 0
tile_width = 160
clock = pygame.time.Clock()
bg = pygame.image.load("sp/backgroung.png")
bg2 = []
for i in range(42):
    bg2.append(pygame.image.load("anim/tmp-" + str(i) + ".gif"))
bg3 = []
for i in range(49):
    bg3.append(pygame.image.load("obama/59030fcb6670428afaf84fc2725db8cbdOpD2YNLj7VDFKzy-" + str(i) + ".png"))

class Block(pygame.sprite.Sprite):
    # это класс кирпичика.
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

    # эта функция читает текстовый файл карты и делает на основании его массив с данными
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map

def generate_level(level):

    # эта функция на основании массива с данными генерирует блоки
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'r' or level[y][x] == 'R':
                Block(level[y][x], False, x, y)
    return new_player, x, y

def menu():

    # это стартовый экран. Он объясняет новому игроку цель игры
    if __name__ == '__main__':
        pygame.init()
        myfont = pygame.font.SysFont('comicsansms', 20, bold=True)
        rules1 = myfont.render('Добро пожаловать в нашу игру "Киберкирпичики!"', False, (255, 255, 255))
        rules2 = myfont.render('Вашей задачей тут будет пройти все 5 уровней, разбивая кирпичи мячиком',
                               False, (255, 255, 255))
        rules3 = myfont.render('Вам надо будет ловить его ракеткой, '
                               'нажимая влево и вправо на клавиатуре', False, (255, 255, 255))
        rules4 = myfont.render('Вам будут встречаться золотые кирпичи, сломав которые вы усилите ваш мячик на 5 сек', False, (255, 255, 255))
        rules5 = myfont.render('Желаем вам удачи! Нажмите любую кнопку, чтобы продолжить', False, (255, 255, 255))
        pygame.display.set_caption('Киберкирпичики')
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
            screen.blit(rules1, (0, 0))
            screen.blit(rules2, (0, 40))
            screen.blit(rules3, (0, 80))
            screen.blit(rules4, (0, 120))
            screen.blit(rules5, (0, 160))
            c += 1
            clock.tick(fps)
            pygame.display.flip()
        main(lvls[lvl])


def main(mapp='sp/map.txt'):

    # это главная функция в проекте, которая является основным игровым процессом
    if __name__ == '__main__':

        # тут по стандарту предзагружается питон и глобальная переменная очков
        global c_score

        pygame.init()
        pygame.display.set_caption('Киберкирпичики')
        screen = pygame.display.set_mode((800, 600))

        running = True
        clock = pygame.time.Clock()

        fps = 30

        # расставляем мячик и ракетку по местам
        sprite.rect.y = 520
        sprite.rect.x = 300
        sprite2.rect.y = 300
        sprite2.rect.x = 400

        # это наши основные текстовые виджеты.
        pygame.font.init()
        myfont = pygame.font.SysFont('comicsansms', 24)
        textsurface = myfont.render('Очки:' + str(c_score), False, (255, 255, 255)) # очки
        textsurface1 = myfont.render('0' + ':' + str(0), False, (255, 255, 255)) # таймер оставшегося времени усиления

        # скорость мяча
        dx = 5
        dy = 5

        # загружаем карту из txt файла
        player, level_x, level_y = generate_level(write_map(mapp))

        maxscore = len(all_sprites3) + len(all_sprites4)
        score = 0
        timer = 0

        # эта переменная отвечает за то, мячик сейчас ускорен или нет
        snd_dir = path.join(path.dirname(__file__), 'sp')
        collide_sound = pygame.mixer.Sound(path.join(snd_dir, 'sfx-4.mp3'))
        col_sound = pygame.mixer.Sound(path.join(snd_dir, 'sfx-15.mp3'))
        a1 = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()

            # двигаем мяч
            sprite2.rect.x += dx
            sprite2.rect.y += dy

            # отрабатываем касания от стенок
            if sprite2.rect.y > 555:

                # если мяч не усилен, то он не умирает
                if a1:
                    dy *= -1
                else:
                    running = False
                    gameover()
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

            # двигаем ракетку, если игрок нажимает кнопки
            if key[pygame.K_RIGHT]:
                sprite.rect.x = sprite.rect.x + 12

            if key[pygame.K_LEFT]:
                sprite.rect.x = sprite.rect.x - 12

            # отрабатываем касания мячика с другими объектами
            if pygame.sprite.collide_mask(sprite, sprite2):
                col_sound.play()
                # отскок от ракетки
                dy *= -1
                dx *= 1
            if pygame.sprite.groupcollide(all_sprites2, all_sprites3, False, True):
                collide_sound.play()
                # отскок мяча от в нижней части блоков
                if sprite2.rect.y == 76 or sprite2.rect.y == 154 or sprite2.rect.y == 232:
                    dy *= 1
                    dx *= -1
                else:
                    dy *= -1
                    dx *= 1
            if pygame.sprite.groupcollide(all_sprites2, all_sprites4, False, True):
                collide_sound.play()
                # касания мяча и усиленных блоков
                a1 = True

                # врубаем режим усиления
                sprite2.image = pygame.image.load('sp/ball_2.png')

                # обновляем таймер относительно текущих кадров в секунду
                timer = 10 * fps

                # увеличиваем скорость так, чтобы избежать неправильного направления полета мяча

                if dx > 0:
                    dx = 10
                else:
                    dx = -10
                if dy > 0:
                    dy = 10
                else:
                    dy = -10
                # отскок мяча от в нижней части блоков

                if sprite2.rect.y == 76 or sprite2.rect.y == 154 or sprite2.rect.y == 232:
                    dy *= -1
                    dx *= 1
                else:
                    dy *= -1
                    dx *= 1
            # тут стартует алгоритм вычисления очков.
            # Дело в том, что иногда мячик может сбить не один блок, а два сразу.
            # Для таких случаев мы сделали алгоритм, который позволяет эту ошибку избежать.
            # Он из количества блоков до удара мячом (score1) вычитает количество блоков, после удара мячом (score)
            # После этого он обновляет счетчик и смотрит, не выиграл ли игрок (не достиг ли он maxscore)

            score1 = score
            all_score = len(all_sprites3) + len(all_sprites4)
            score = maxscore - all_score
            c_score += (score - score1) * 100

            # Обновляем очки и таймер
            textsurface = myfont.render(str(c_score), False, (255, 25, 255))
            textsurface1 = myfont.render('0:' + str(timer//fps), False, (255, 25, 255))

            # Обновляем таймер
            if timer == 0:
                if dx > 0:
                    dx = 5
                else:
                    dx = -5
                if dy > 0:
                    dy = 5
                else:
                    dy = -5
                a1 = False
                sprite2.image = pygame.image.load('sp/ball.png')
            if a1 == True:
                timer -= 1
            if score == maxscore:
                running = False
                win()

            # остается только отрисовать все, что мы сделали
            screen.blit(bg, (0, 0))
            try:
                all_sprites.draw(screen)
                all_sprites2.draw(screen)
                all_sprites3.draw(screen)
            except Exception as e:
                print(e)
            clock.tick(fps)
            screen.blit(textsurface, (0, 0))
            screen.blit(textsurface1, (380, 0))
            pygame.display.flip()


def win():
    # эта функция одновременно отвечает за переход между уровнями и за концовку игры
    global lvl
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()

    # все определяется в этой развилке:
    if lvl < 4:
        sprite.image = pygame.image.load('sp/win.png')
    else:
        sprite.image = pygame.image.load('sp/fin.png')
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    all_sprites.add(sprite)
    clock = pygame.time.Clock()
    running = True
    fps = 100
    snd_dir = path.join(path.dirname(__file__), 'sp')
    dance = pygame.mixer.Sound(path.join(snd_dir, 'wow.mp3'))
    while running:
        dance.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                running = False
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

    # а также тут. Если уровень последний, то мы не начинаем новую игру а просто закрываем окно
    if lvl < 4:
        lvl += 1
        main(lvls[lvl])

def obama():
    global lvl
    lvl = 5
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    # все определяется в этой развилке:
    sprite.image = pygame.image.load('sp/fin.png')
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    all_sprites.add(sprite)
    clock = pygame.time.Clock()
    running = True
    fps = 100
    snd_dir = path.join(path.dirname(__file__), 'sp')
    dance = pygame.mixer.Sound(path.join(snd_dir, 'wow.mp3'))
    while running:
        dance.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                running = False
        for i in range(len(bg3)):
            sprite.image = pygame.image.load(i)
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = 0
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

    # а также тут. Если уровень последний, то мы не начинаем новую игру а просто закрываем окно
    if lvl < 4:
        lvl += 1
        main(lvls[lvl])

def gameover():

    # это экран конца игры
    size = 700, 460
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


# ну и при запуске игры мы запускаем стартовое меню
if __name__ == "__main__":
    menu()