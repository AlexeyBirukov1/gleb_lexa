import pygame
import sys

size = width, height = 800, 600
black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    ball_image = pygame.image.load("sp/ball.png")
    ball_rect = ball_image.get_rect()
    ball_rect.x = 101
    ball_rect.y = 101
    game_over = False
    dx = 2
    dy = 2
    platform_x = 250
    platform_y = 500
    move_right = False
    move_left = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)
        pygame.draw.rect(screen, (255, 255, 255), (platform_x, platform_y, 150, 20))
        screen.blit(ball_image, ball_rect)
        ball_rect.x += dx
        ball_rect.y += dy
        if ball_rect.y > 500 or ball_rect.y < 0:
            dy *= -1
        if ball_rect.x > 700 or ball_rect.x < 0:
            dx *= -1
        # ------------------------------------------
        if ball_rect.y > platform_y - 110 and ball_rect.x > platform_x and ball_rect.x < platform_x + 150:
            dy *= -1
        if move_left:
            platform_x -= 1
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()