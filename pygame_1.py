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
        self.bg = pygame.image.load("sp/backgroung.png")
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
                    screen.blit(self.bg, (0, 0))
                    all_sprites.draw(screen)
                    clock.tick(fps)
                    pygame.display.flip()

                pygame.quit()
        if __name__ == "__main__":
            main()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
