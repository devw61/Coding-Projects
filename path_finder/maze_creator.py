import pygame as pg
from random import choice
import time

res = width, height = 1202, 902
gap = 25
cols, rows = width // gap, height // gap
start_time = time.time()
rand = 0


pg.init()
sc = pg.display.set_mode(res)
clock = pg.time.Clock()

class Node:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"top": True, "bottom": True, "right": True, "left":True}
        self.visited = False

    def draw_current_node(self):
        x, y = self.x * gap, self.y * gap
        pg.draw.rect(sc, pg.Color('saddlebrown'), (x+2,y+2, gap-2, gap-2))

    def draw(self):
        x,y = self.x * gap, self.y * gap
        if self.visited:
            pg.draw.rect(sc, pg.Color('black'), (x,y,gap,gap))

        if self.walls['top']:
            pg.draw.line(sc, pg.Color('darkorange'), (x,y), (x+gap,y), 2)
        if self.walls['bottom']:
            pg.draw.line(sc, pg.Color('darkorange'), (x,y+gap), (x+gap,y+gap), 2)
        if self.walls['right']:
            pg.draw.line(sc, pg.Color('darkorange'), (x+gap,y), (x+gap,y+gap), 2)
        if self.walls['left']:
            pg.draw.line(sc, pg.Color('darkorange'), (x,y), (x,y+gap), 2)

    def check_cell(self, x, y):
        find_index = lambda x,y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x,y)]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x,self.y - 1)
        bottom = self.check_cell(self.x,self.y + 1)
        left = self.check_cell(self.x - 1,self.y)
        right = self.check_cell(self.x + 1,self.y)
        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)

        return choice(neighbors) if neighbors else False
    
    def skip_check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x,self.y - 1)
        bottom = self.check_cell(self.x,self.y + 1)
        left = self.check_cell(self.x - 1,self.y)
        right = self.check_cell(self.x + 1,self.y)
        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)

        return choice(neighbors) if len(neighbors) > 1 else False

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    if dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
        
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    if dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False
    

grid_cells = [Node(col, row) for row in range(rows) for col in range (cols)]
current_cell = grid_cells[0]
stack = []
visited = 0

while True:
    sc.fill(pg.Color("darkslategray"))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_node()

    next_cell = current_cell.check_neighbors()
    # skip_cell = current_cell.skip_check_neighbors()
    # if skip_cell:
    #     next_cell.visited = True
    #     stack.append(current_cell)
    #     remove_walls(current_cell,next_cell)
    #     current_cell = next_cell
    if next_cell :
        remove_walls(current_cell,next_cell)
        stack.append(current_cell)
        current_cell = next_cell
        next_cell.visited = True
    elif stack:
        while stack and current_cell.check_neighbors() == False and len(stack) != 1:
            current_cell = stack.pop()
        else :
            current_cell == stack.pop()
            

    pg.display.flip()
    clock.tick(200)
    if stack == [] and rand == 0:
        print("--- %s seconds ---" % (time.time() - start_time))
        rand += 1
