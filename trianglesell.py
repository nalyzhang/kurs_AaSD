import pygame

res = width, height = 800, 800
cell = 20
w, h = 1 + width // cell, 4 * height // cell
fps = 300

pygame.init()
field = pygame.display.set_mode(res)
clock = pygame.time.Clock()
cur_cell = [[0 for i in range(h)] for j in range(w)]
cur_cell[w//2][h//2] = 3000


n = 0 
while True:
    if (n == w*h): break
    n = 0
    field.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    
    
    for x in range(w):
        for y in range(h):
            
            tmp = cur_cell[x][y]
            if y%4 == 0:
                if cur_cell[x][y] > 2:
                    if x != 0:
                        cur_cell[x-1][y+1] += 1
                    cur_cell[x][y+1] += 1
                    if y != 0:
                        cur_cell[x][y-1] += 1
                    cur_cell[x][y] -= 3
                if cur_cell[x][y] == 0:
                    pygame.draw.polygon(field, pygame.Color('light yellow'), ((x*cell,(y+2)*cell//4),((2*x-1)*cell//2,(y)*cell//4), ((2*x+1)*cell//2, (y)*cell//4)))
                elif cur_cell[x][y] == 1:
                    pygame.draw.polygon(field, pygame.Color('yellow'), ((x*cell,(y+2)*cell//4),((2*x-1)*cell//2,(y)*cell//4), ((2*x+1)*cell//2, (y)*cell//4)))
                elif cur_cell[x][y] == 2:
                    pygame.draw.polygon(field, pygame.Color('gold'), ((x*cell,(y+2)*cell//4),((2*x-1)*cell//2,(y)*cell//4), ((2*x+1)*cell//2, (y)*cell//4)))
                else:
                    pygame.draw.polygon(field, pygame.Color('green'), ((x*cell,(y+2)*cell//4),((2*x-1)*cell//2,(y)*cell//4), ((2*x+1)*cell//2, (y)*cell//4)))
                
            elif y%4 == 1:
                if cur_cell[x][y] > 2:
                    cur_cell[x][y+1] += 1
                    if x != w-1:
                        cur_cell[x+1][y-1] += 1
                    cur_cell[x][y-1] += 1
                    cur_cell[x][y] -= 3
                    
                    
                if cur_cell[x][y] == 0:
                    pygame.draw.polygon(field, pygame.Color('light yellow'), ((x*cell,(y+1)*cell//4),((x+1)*cell,(y+1)*cell//4),((2*x+1)*cell//2,((y-1))*cell//4)))
                elif cur_cell[x][y] == 1:
                    pygame.draw.polygon(field, pygame.Color('yellow'), ((x*cell,(y-3)*cell//4 + cell),((x+1)*cell,(y-3)*cell//4 + cell),((2*x+1)*cell//2,((y-1))*cell//4)))
                elif cur_cell[x][y] == 2:
                    pygame.draw.polygon(field, pygame.Color('gold'), ((x*cell,(y-3)*cell//4 + cell),((x+1)*cell,(y-3)*cell//4 + cell),((2*x+1)*cell//2,((y-1))*cell//4)))
                else:
                    pygame.draw.polygon(field, pygame.Color('green'), ((x*cell,(y-3)*cell//4 + cell),((x+1)*cell,(y-3)*cell//4 + cell),((2*x+1)*cell//2,((y-1))*cell//4)))

            elif y%4 == 2:
                if cur_cell[x][y] > 2:
                    cur_cell[x][y+1] += 1
                    cur_cell[x][y-1] += 1
                    if x != w-1:
                        cur_cell[x+1][y+1] += 1
                    cur_cell[x][y] -= 3
                if cur_cell[x][y] == 0:
                    pygame.draw.polygon(field, pygame.Color('light yellow'), ((x*cell,y*cell//4),((x+1)*cell,y*cell//4),((2*x+1)*cell//2,(y+2)*cell//4)))
                elif cur_cell[x][y] == 1:
                    pygame.draw.polygon(field, pygame.Color('yellow'), ((x*cell,(y-4)*cell//4 + cell),((x+1)*cell,(y-4)*cell//4 + cell),((2*x+1)*cell//2,((y+2))*cell//4)))
                elif cur_cell[x][y] == 2:
                    pygame.draw.polygon(field, pygame.Color('gold'), ((x*cell,(y-4)*cell//4 + cell),((x+1)*cell,(y-4)*cell//4 + cell),((2*x+1)*cell//2,((y+2))*cell//4)))
                else:
                    pygame.draw.polygon(field, pygame.Color('green'), ((x*cell,(y-4)*cell//4 + cell),((x+1)*cell,(y-4)*cell//4 + cell),((2*x+1)*cell//2,((y+2))*cell//4)))

            elif y%4 == 3:
                if cur_cell[x][y] > 2:
                    cur_cell[x][y-1] += 1
                    if x != 0:
                        cur_cell[x-1][y-1] += 1
                    cur_cell[x][y+1] += 1
                    cur_cell[x][y] -= 3
                if cur_cell[x][y] == 0:
                    pygame.draw.polygon(field, pygame.Color('light yellow'), (((2*x-1)*cell//2,(y+1)*cell//4),((2*x+1)*cell//2,(y+1)*cell//4),(x*cell,(y-1)*cell//4)))
                elif cur_cell[x][y] == 1:
                    pygame.draw.polygon(field, pygame.Color('yellow'), (((2*x-1)*cell//2,(y+1)*cell//4),((2*x+1)*cell//2,(y+1)*cell//4),(x*cell,(y-1)*cell//4)))
                elif cur_cell[x][y] == 2:
                    pygame.draw.polygon(field, pygame.Color('gold'), (((2*x-1)*cell//2,(y+1)*cell//4),((2*x+1)*cell//2,(y+1)*cell//4),(x*cell,(y-1)*cell//4)))
                else:
                    pygame.draw.polygon(field, pygame.Color('green'), (((2*x-1)*cell//2,(y+1)*cell//4),((2*x+1)*cell//2,(y+1)*cell//4),(x*cell,(y-1)*cell//4)))

            if tmp == cur_cell[x][y]: n += 1
    pygame.display.flip()
    clock.tick(fps)



'''
    [pygame.draw.line(field, pygame.Color('grey'), (0, y), (width, y)) for y in range(cell//2, height, cell//2)]
    [pygame.draw.line(field, pygame.Color('grey'), (x, 0), (0, x)) for x in range(cell//2, width+height, cell)]
    [pygame.draw.line(field, pygame.Color('grey'), (y, 0), (height, height-y)) for y in range(cell//2, width, cell)]
    [pygame.draw.line(field, pygame.Color('grey'), (0, y), (height-y, height)) for y in range(cell//2, height, cell)]

'''
