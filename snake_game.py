import pygame 
import random
import time

# window size

window_x = 450
window_y = 300

pygame.init()
window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# fruit init
fruit_start = [random.randrange(10, window_x//10)*10, random.randrange(10, window_y//10)*10]

# snake init
direction = 'RIGHT'
direction_q = direction
snake_start = [100, 100]
snake_body = [[100,100],
              [90,100],
              [80,100],
              [70, 100]]

score = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_q = 'UP'
            if event.key == pygame.K_DOWN:
                direction_q = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction_q = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction_q = 'RIGHT'
   
    if direction_q == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if direction_q == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if direction_q == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if direction_q == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    temp_snake_start = snake_body[0].copy()
    if direction == 'UP':
        snake_body[0][1] -= 10
    if direction == 'DOWN':
        snake_body[0][1] += 10
    if direction == 'LEFT':
        snake_body[0][0] -= 10
    if direction == 'RIGHT':
        snake_body[0][0] += 10

    snake_body.insert(1, temp_snake_start)
    snake_body.pop(-1)

    window.fill(pygame.Color(0,0,0))

    for pos in snake_body[1:]:
        if (pos == snake_body[0]):
            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render('Your Score is : ' + str(score), True, pygame.Color(255,0,0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (window_x/2, window_y/4)
            window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            quit()


    if (snake_body[0][0] < 0 or snake_body[0][1] < 0 or snake_body[0][0] > window_x or snake_body[0][1] > window_y):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, pygame.Color(255,0,0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    if (snake_body[0] == fruit_start):
            score += 1
            if direction == 'UP':
                snake_body.append([snake_body[-1][0], snake_body[-1][1] +10])
            if direction == 'DOWN':
                snake_body.append([snake_body[-1][0], snake_body[-1][1] -10])
            if direction == 'LEFT':
                snake_body.append([snake_body[-1][0] +10, snake_body[-1][1]])
            if direction == 'RIGHT':
                snake_body.append([snake_body[-1][0] -10, snake_body[-1][1]])
            fruit_start = [random.randrange(10, window_x//10)*10, random.randrange(10, window_y//10)*10]

    for position in snake_body:
        pygame.draw.rect(window, pygame.Color(100, 200, 130),
                         pygame.Rect(position[0], position[1], 10, 10))
    pygame.draw.rect(window, pygame.Color(255, 0, 0),
                         pygame.Rect(fruit_start[0], fruit_start[1], 10, 10))
    

    score_font = pygame.font.SysFont('times new roman', 10)
    score_surface = score_font.render('Score : ' + str(score), True, pygame.Color(150, 100, 200))
    score_rect = score_surface.get_rect()
    window.blit(score_surface, score_rect)
    
    pygame.display.update()
    fps.tick(10)