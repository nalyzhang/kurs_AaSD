import pygame
import math

HONEY = (236,151,6)
BRONZE = (178,86,13)

RES = width, height = 800, 800
cell = 10
wt = cell*2/math.sqrt(3)
ht = cell
w, h = math.floor(width // wt), 2 * height // ht  -1
fps = 3000

pygame.init()
field = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


cur_cell = [[0 for i in range(h)] for j in range(w)]
cur_cell[(w-1)//3][h//2] = 3000
count = 0

while True:
    if count == h*w: break
    count = 0
    field.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    for y in range(h):
        for x in range(w):
            
            tmp = cur_cell[x][y]
            
            if (cur_cell[x][y] > 5):
                if (x != (y%2)-1):
                    if y != 0:
                        cur_cell[x+(y%2)-1][y-1] += 1
                    if y != h-1:
                        cur_cell[x+(y%2)-1][y+1] += 1
                if (y > 1):
                    cur_cell[x][y-2] += 1
                if (y < h-2):
                    cur_cell[x][y+2] += 1
                if (x != w - (y%2)):
                    if y != 0:
                        cur_cell[x+(y%2)][y-1] += 1
                    if y != h-1:
                        cur_cell[x+(y%2)][y+1] += 1
                cur_cell[x][y] -= 6
            
            if y%2 == 0:
                n = 0
            if y%2 == 1:
                n = 3*wt/4
            
            if cur_cell[x][y] == 0:
                pygame.draw.polygon(field, pygame.Color('light yellow'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 1:
                pygame.draw.polygon(field, pygame.Color('yellow'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 2:
                pygame.draw.polygon(field, pygame.Color('gold'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 3:
                pygame.draw.polygon(field, pygame.Color(HONEY), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 4:
                pygame.draw.polygon(field, pygame.Color('orange'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 5:
                pygame.draw.polygon(field, pygame.Color(BRONZE), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            else:
                pygame.draw.polygon(field, pygame.Color('blue'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))

            if tmp == cur_cell[x][y]: count += 1
    pygame.display.flip()
    clock.tick(fps)

'''
            if cur_cell[x][y] == 0:
                pygame.draw.polygon(field, pygame.Color('red'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 1:
                pygame.draw.polygon(field, pygame.Color('orange'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 2:
                pygame.draw.polygon(field, pygame.Color('yellow'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 3:
                pygame.draw.polygon(field, pygame.Color('green'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 4:
                pygame.draw.polygon(field, pygame.Color('blue'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            elif cur_cell[x][y] == 5:
                pygame.draw.polygon(field, pygame.Color('purple'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
            else:
                pygame.draw.polygon(field, pygame.Color('light blue'), ((x*6*wt/4+n, (y+1)*ht/2),((6*x+1)*wt/4+n,y*ht/2),((x*6+3)*wt/4+n,y*ht/2),((6*x+4)*wt/4+n,(y+1)*ht/2),((x*6+3)*wt/4+n,(y+2)*ht/2),((x*6+1)*wt/4+n,(y+2)*ht/2)))
'''
