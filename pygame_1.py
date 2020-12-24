import os
import sys
import pygame
import copy
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QPushButton, QLineEdit, \
    QPlainTextEdit, QMessageBox, QFileDialog, QComboBox

from d import Ui_MainWindow
import sqlite3

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.select)
        self.pushButton_7.clicked.connect(self.life)

    def life(self):
        size = 180, 250
        screen = pygame.display.set_mode(size)

        class Board:
            # создание поля
            def __init__(self, width, height, left=10, top=10, cell_size=10):
                self.width = width
                self.height = height
                self.board = [[0] * width for _ in range(height)]
                # значения по умолчанию
                self.left = left
                self.top = top
                self.cell_size = cell_size
                self.set_view(left, top, cell_size)

            # настройка внешнего вида
            def set_view(self, left, top, cell_size):
                self.left = left
                self.top = top
                self.cell_size = cell_size

            def render(self):
                for x in range(self.width):
                    for y in range(self.height):
                        pygame.draw.rect(screen, pygame.Color('white'), (x * self.cell_size + self.left,
                                                                         y * self.cell_size + self.top, self.cell_size,
                                                                         self.cell_size), 1)

            def on_click(self, cell):
                pass

            def get_cell(self, mous_pos):
                x = (mous_pos[0] - self.left) // self.cell_size
                y = (mous_pos[1] - self.top) // self.cell_size
                if x < 0 and x >= self.width or y < 0 and y > self.height:
                    return None
                else:
                    return x, y

            def get_click(self, mous_pos):
                cell = self.get_cell(mous_pos)
                if cell:
                    self.on_click(cell)

        class Life(Board):
            def __init__(self, width, height, left=10, top=10, cell_size=10):
                super().__init__(width, height, left, top, cell_size)

            def on_click(self, cell):
                self.board[cell[1]][cell[0]] = (self.board[cell[1]][cell[0]] + 1) % 2

            def render(self, screen):
                for y in range(self.height):
                    for x in range(self.width):
                        if self.board[y][x]:
                            pygame.draw.rect(screen, pygame.Color('green'), (x * self.cell_size + self.left,
                                                                             y * self.cell_size + self.top,
                                                                             self.cell_size,
                                                                             self.cell_size))
                        pygame.draw.rect(screen, pygame.Color('white'), (x * self.cell_size + self.left,
                                                                         y * self.cell_size + self.top, self.cell_size,
                                                                         self.cell_size), 1)

            def next_move(self):
                tmp_board = copy.deepcopy(self.board)
                for y in range(self.height):
                    for x in range(self.width):
                        s = 0
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if (x + dx < 0 or x + dx >= self.width or y + dy < 0
                                        or y + dy >= self.height):
                                    continue
                                s += self.board[y + dy][x + dx]
                        s -= self.board[y][x]
                        if s == 3:
                            tmp_board[y][x] = 1
                        elif s < 2 or s > 3:
                            tmp_board[y][x] = 0
                self.board = copy.deepcopy(tmp_board)

        size = 600, 400
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Жизнь')
        board = Life(30, 20, 10, 10, 18)
        running = True
        time_on = False
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    board.get_click(event.pos)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    time_on = not time_on
            screen.fill((0, 0, 0))
            board.render(screen)
            if time_on:
                board.next_move()
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def select(self):
        def main():
            WHITE = (255, 255, 255)
            PINK = (230, 50, 230)
            ORANGE = (255, 150, 100)
            clock = pygame.time.Clock()
            circles = []
            speed = []
            speedvorot = []
            vorota = []

            r = 10
            if __name__ == '__main__':
                pygame.init()
                size = width, height = 800, 600
                pygame.display.set_caption('ШАРЫ')
                screen = pygame.display.set_mode(size)
                screen2 = pygame.display.set_mode(size)
                running = True
                circles.append(list((400, 300)))
                pygame.draw.line(screen, (ORANGE), (0, 200), (0, 260), width=25)
                pygame.draw.line(screen, (ORANGE), (800, 200), (800, 260), width=25)
                y_movement1 = 267.5
                y_movement2 = 267.5
                x_velocity = 300
                y_velocity = 300
                gy = 25
                sp2 = 765
                sp1 = 35
                while running:
                    if y_velocity < gy:
                        x_velocity += 5
                        y_velocity += 5
                    if x_velocity == 600:
                        x_velocity = 300
                        y_velocity = 300
                    if x_velocity == 0:
                        x_velocity = 300
                        y_velocity = 300
                    if x_velocity + 7.5 == sp2 and y_velocity < 300:
                        x_velocity -= 5
                        y_velocity += 5
                    if x_velocity + 7.5 == sp2 and y_velocity > 300:
                        x_velocity -= 5
                        y_velocity -= 5
                    if x_velocity == sp1 and y_velocity < 300:
                        x_velocity += 5
                        y_velocity += 5
                    if x_velocity == sp1 and y_velocity > 300:
                        x_velocity += 5
                        y_velocity -= 5

                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_w] and y_movement1 > 25:
                        y_movement1 -= 1.8
                    if keys[pygame.K_s] and y_movement1 < 575 - 25 - 6:
                        y_movement1 += 1.8
                    if keys[pygame.K_UP] and y_movement2 > 25:
                        y_movement2 -= 1.8
                    if keys[pygame.K_DOWN] and y_movement2 < 550 - 25 - 6:
                        y_movement2 += 1.8


                    speed.append([1, -0.5])
                    for event in pygame.event.get():
                        # при закрытии окна
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                    screen2.fill(WHITE)
                    screen.fill(WHITE)
                    for i in range(len(circles)):
                        for x in (0, 1):
                            if circles[i][x] + r >= size[x] or circles[i][x] - r <= 0:
                                speed[i][x] = -speed[i][x]

                            circles[i][x] += speed[i][x]
                        pygame.draw.circle(screen2, (ORANGE), circles[i], r)
                        pygame.draw.rect(screen, (PINK), (sp1, y_movement1, 10, 100))
                        pygame.draw.rect(screen, (ORANGE), (sp2, y_movement2, 10, 100))
                    screen.blit(screen2, (0, 0))

                    # обновление экрана
                    pygame.display.flip()
                    fps = 200
                    clock.tick(fps)

                pygame.quit()
        if __name__ == "__main__":
            main()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
