#logic.py this will implement all of the functions used by 2048

#We need to be able to generate random numbers so we are going to import that random library
import random

#This function will set up the game

def print_grid(grid):
    for row in grid:
        print(" | ".join("{:^5}".format(str(cell) if cell != 0 else '.') for cell in row))
        print("-" * 29)
    print()


def start_game():
    grid = []
    for i in range(4):
        grid.append([0] * 4)
    print("Commands are as follows: ")
    print("w is to go up")
    print("s is to go down")
    print("a is to go left")
    print("d is to go right")
    add_new_2(grid)
    print("add_new_2 works")
    return grid

#This function will keep adding a new 2 tile
#to the grid
def add_new_2(grid):
    r = random.randint(0,3)
    c = random.randint(0,3)

    while grid[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    grid[r][c] = 2


#Return the current state of the game
def get_current_state(grid):

    #Check to see if 2048 exists
    for i in range(4):
        for j in range(4):
            if(grid[i][j] == 2048):
                return "YOU WON!"
    
    #Look to find an empty space
    for i in range(4):
        for j in range(4):
            if(grid[i][j] == 0):
                return "GAME IS NOT OVER"
            
    #Check to see if nodes can be merged
    #For more visualization of this process then just 
    #draw it out you silly goober. Silly mongoose. 
    for i in range(3):
        for j in range(3):
            if(grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]):
                return "GAME IS NOT OVER"
    
    for j in range(3):
        if(grid[3][j] == grid[3][j+1]):
            return "GAME IS NOT OVER"
        
    for i in range(3):
        if(grid[i][3] == grid[i+1][3]):
            return "GAME IS NOT OVER"
        
    return "GAME OVER"

#This function is made to compress the 
#board. After every step and move
def compress(grid):

    changed = False

    #empty board
    new_grid = []

    for i in range(4):
        new_grid.append([0] * 4)

    for i in range(4):
        pos = 0

        for j in range(4):
            if(grid[i][j] != 0):
                new_grid[i][pos] = grid[i][j]
                if(j != pos):
                    changed = True
                pos += 1

    return new_grid,changed

#This will merge all squares together
def merge(grid):
    changed = False

    for i in range(4):
        for j in range(3):

            if(grid[i][j] == grid[i][j+1] and grid[i][j] != 0 ):
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0

                changed = True


    return grid, changed

def reverse(grid):
    new_grid=[]
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3-j])
    return new_grid

def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i])
    return new_grid

def move_left(grid):
    new_grid, changed1 = compress(grid)

    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    new_grid, temp = compress(new_grid)

    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)

    new_grid, changed = move_left(new_grid)

    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

print('teseting alias commands out')