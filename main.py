"""
Dougla Kosvoski
Press Space on the keyboard to push the ball down and make it bounce
"""

import pygame

canvas_width, canvas_height = 800, 600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
fps = pygame.time.Clock()

blue  = (80, 120, 200)
white = (255,255,255)

speed, gravity = 0, 0
radius = 40

y = canvas_height-100-radius
inf_limit = canvas_height-100

def background(color):
    lineX, lineY = 30, canvas_height-100
    pygame.draw.rect(canvas, color, [0,0,canvas_width,canvas_height])
    pygame.draw.line(canvas, white, [lineX, lineY] , [canvas_width - lineX, lineY], 2)

def object(color):
    x = int(canvas_width / 2)
    pygame.draw.circle(canvas, color, (x, int(y)), radius, 0)

while True:
    background(blue)
    object(white)

    if y+radius <= inf_limit:
        speed -= gravity
    elif y+radius+2 > inf_limit:
        speed *= -1
        if gravity > -5:
            gravity *= 1.2
        else:
            speed = 0
            gravity = 0
            y = inf_limit-radius
    y += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                speed = 20
                gravity = (speed/25) * -1

    fps.tick(60)
    pygame.display.update()
