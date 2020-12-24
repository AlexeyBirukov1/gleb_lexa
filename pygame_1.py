import os
import sys
import pygame
import copy
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QPushButton, QLineEdit, \
    QPlainTextEdit, QMessageBox, QFileDialog, QComboBox

from d import Ui_MainWindow
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('sp/paddle_big.png')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.select)

    def select(self):
        def main():
            WHITE = (255, 255, 255)
            PINK = (230, 50, 230)
            ORANGE = (255, 150, 100)
            clock = pygame.time.Clock()
            circles = []
            speed = []

            r = 10
            if __name__ == '__main__':
                pygame.init()
                size = width, height = 800, 600
                pygame.display.set_caption('ШАРЫ')
                screen = pygame.display.set_mode(size)
                screen2 = pygame.display.set_mode(size)
                running = True
                circles.append(list((400, 300)))
                y_movement1 = 267.5
                y_movement2 = 267.5
                x_velocity = 300
                y_velocity = 300
                gy = 25
                sp2 = 765
                sp1 = 35
                MYEVENTTYPE = pygame.USEREVENT
                pygame.time.set_timer(MYEVENTTYPE, 100)
                running = True
                clock = pygame.time.Clock()
                fps = 100
                sprite.rect.y = 550
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    key = pygame.key.get_pressed()
                    if key[pygame.K_RIGHT]:
                        sprite.rect.x = sprite.rect.x + 2
                    if key[pygame.K_LEFT]:
                        sprite.rect.x = sprite.rect.x - 2
                    screen.fill(pygame.Color(WHITE))
                    all_sprites.draw(screen)
                    clock.tick(fps)
                    pygame.display.flip()
                # while running:
                #     if y_velocity < gy:
                #         x_velocity += 5
                #         y_velocity += 5
                #     if x_velocity == 600:
                #         x_velocity = 300
                #         y_velocity = 300
                #     if x_velocity == 0:
                #         x_velocity = 300
                #         y_velocity = 300
                #     if x_velocity + 7.5 == sp2 and y_velocity < 300:
                #         x_velocity -= 5
                #         y_velocity += 5
                #     if x_velocity + 7.5 == sp2 and y_velocity > 300:
                #         x_velocity -= 5
                #         y_velocity -= 5
                #     if x_velocity == sp1 and y_velocity < 300:
                #         x_velocity += 5
                #         y_velocity += 5
                #     if x_velocity == sp1 and y_velocity > 300:
                #         x_velocity += 5
                #         y_velocity -= 5
                #
                #     keys = pygame.key.get_pressed()
                #
                #     if keys[pygame.K_w] and y_movement1 > 25:
                #         y_movement1 -= 1.8
                #     if keys[pygame.K_s] and y_movement1 < 575 - 25 - 6:
                #         y_movement1 += 1.8
                #     if keys[pygame.K_UP] and y_movement2 > 25:
                #         y_movement2 -= 1.8
                #     if keys[pygame.K_DOWN] and y_movement2 < 550 - 25 - 6:
                #         y_movement2 += 1.8
                #
                #
                #     speed.append([1, -0.5])
                #     for event in pygame.event.get():
                #         # при закрытии окна
                #         if event.type == pygame.QUIT:
                #             running = False
                #         if event.type == pygame.KEYUP:
                #             if event.key == pygame.K_ESCAPE:
                #                 running = False
                #     screen2.fill(WHITE)
                #     screen.fill(WHITE)
                #     for i in range(len(circles)):
                #         for x in (0, 1):
                #             if circles[i][x] + r >= size[x] or circles[i][x] - r <= 0:
                #                 speed[i][x] = -speed[i][x]
                #
                #             circles[i][x] += speed[i][x]
                #         pygame.draw.circle(screen2, (ORANGE), circles[i], r)
                #         pygame.draw.rect(screen, (PINK), (sp1, y_movement1, 10, 100))
                #         pygame.draw.rect(screen, (ORANGE), (sp2, y_movement2, 10, 100))
                #     screen.blit(screen2, (0, 0))
                #
                #     # обновление экрана
                #     pygame.display.flip()
                #     fps = 200
                #     clock.tick(fps)

                pygame.quit()
        if __name__ == "__main__":
            main()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
