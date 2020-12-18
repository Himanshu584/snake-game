
from typing import Optional, Any
import pygame
import random

# initialize game
pygame.init()
# colours
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
gold =(255,223,0)
# setting up display window
screen_width = 900
screen_height = 600
# display
game_window = pygame.display.set_mode((screen_width, screen_height))
# game title
pygame.display.set_caption("HIMANSHU'S SNAKE")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color )
    game_window.blit(screen_text, [x, y])


def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((0, 0, 0))
        text_screen('welcome to mysnake', gold, 260, 250)
        text_screen('Press Space Bar To Play', gold, 233, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# GAME-LOOP
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    vel_x = 0
    vel_y = 0
    snk_list = []
    snk_length = 1
    with open('hiscore.txt', 'w') as f:
        hiscore = f.write('0')

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            game_window.fill(black)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_velocity
                        vel_y = 0

                    if event.key == pygame.K_LEFT:
                        vel_x = - init_velocity
                        vel_y = 0

                    if event.key == pygame.K_UP:
                        vel_y = - init_velocity
                        vel_x = 0

                    if event.key == pygame.K_DOWN:
                        vel_y = init_velocity
                        vel_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y

            if abs(snake_x - food_x) < 9 and abs(snake_y - food_y) < 9:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            game_window.fill(black)
            text_screen("Score: " + str(score) + "  Hiscore: " + str(hiscore), red, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            plot_snake(game_window, white, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()