import pygame
pygame.init()
import random
speed = 0.5
score = 0

start = True
x= 300
y = 300
x_food = random.randint(7, 593)
y_food = random.randint(7, 593)
width, haight = 600, 600 
font = pygame.font.SysFont(None, 24)


def points(window, text, x , y):
    img = font.render(text, True, (255,255,255))
    window.blit(img,(x,y))


window = pygame. display.set_mode((width, haight))
pygame.display.set_caption('Snake game')
running = True
while running:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            running = False 
    window.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    if x == 595  or y == 595 or x == 5 or y == 5:
        running = False

    s = "score: " + str(score)
    points(window,s , 0,0)
    food = pygame.draw.circle(window, (0, 125, 125), (x_food, y_food), 7)
    snake = pygame.draw.rect(window, (255, 0, 0), (x, y, 25, 25))
    
    pygame.display.update()
    if snake.colliderect(food):
        score += 1
        x_food = random.randint(7, 593)
        y_food = random.randint(7, 593)
   














pygame.quit()

