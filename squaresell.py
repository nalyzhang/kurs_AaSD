import pygame
from random import randint
from copy import deepcopy

RES = width, height = 610, 610
cell = 10
w, h = width // cell, height // cell
fps = 300
pygame.init()
field = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


cur_cell = [[0 for i in range(w)] for j in range(h)]
cur_cell[w//2][h//2] = 3000
n = 0 
while True:
    if n == h*w: break
    n = 0
    
    field.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #[pygame.draw.line(field, pygame.Color('grey'), (x, 0), (x, height)) for x in range(0, width, cell)]
    #[pygame.draw.line(field, pygame.Color('grey'), (0, y), (width, y)) for y in range(0, height, cell)]
    
    for x in range(w):
        for y in range(h):

            tmp = cur_cell[x][y]
            
            if cur_cell[x][y] > 3:
                if x != 0:
                    cur_cell[x-1][y] += 1
                if x != w-1:
                    cur_cell[x+1][y] += 1
                if y != 0:
                    cur_cell[x][y-1] += 1
                if y != h-1:
                    cur_cell[x][y+1] += 1
                cur_cell[x][y] -= 4
                
            if cur_cell[x][y] == 0:
                pygame.draw.rect(field, pygame.Color('light yellow'), (x * cell, y * cell, cell, cell))
            elif cur_cell[x][y] == 1:
                pygame.draw.rect(field, pygame.Color('yellow'), (x * cell, y * cell, cell, cell))
            elif cur_cell[x][y] == 2:
                pygame.draw.rect(field, pygame.Color('gold'), (x * cell, y * cell, cell, cell))
            elif cur_cell[x][y] == 3:
                pygame.draw.rect(field, pygame.Color('orange'), (x * cell, y * cell, cell, cell))
            else:
                pygame.draw.rect(field, pygame.Color('green'), (x * cell, y * cell, cell, cell))

            if tmp == cur_cell[x][y]: n+= 1
    pygame.display.flip()
    clock.tick(fps)
