import os
import sys
import pygame
import copy
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QPushButton, QLineEdit, \
    QPlainTextEdit, QMessageBox, QFileDialog, QComboBox

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


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bg = pygame.image.load("sp/backgroung.png")
        self.pushButton_3.clicked.connect(self.select)

    def select(self):
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
                    if sprite2.rect.y > 525 or sprite2.rect.y < 0:
                        dy *= -1
                    if sprite2.rect.x > 725 or sprite2.rect.x < 0:
                        dx *= -1
                    if sprite2.rect.x == sprite.rect.x and sprite2.rect.y == 550:
                        dy *= -1
                    # ------------------------------------------
                    if key[pygame.K_RIGHT]:
                        sprite.rect.x = sprite.rect.x + 2
                    if key[pygame.K_LEFT]:
                        sprite.rect.x = sprite.rect.x - 2
                    screen.blit(self.bg, (0, 0))
                    try:
                        all_sprites.draw(screen)
                        all_sprites2.draw(screen)
                    except Exception as e:
                        print(e)
                    clock.tick(fps)
                    pygame.display.flip()

                pygame.quit()
        if __name__ == "__main__":
            main()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
