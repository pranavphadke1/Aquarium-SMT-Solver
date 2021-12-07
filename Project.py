from z3 import *

#Corresponds to Instance1 Image
#6x6 easy
instance1 = ((3,5,3,3,3,5), #Column filling requirements
            (1,1,1,1,1,1), #Top row of horizontal walls
            (2,1,0,1,1,0,0,1), #Vertical walls in row 1
            (1,1,0,0,0,1), #Horizontal walls between rows 1&2
            (4,1,0,0,1,0,1,1), #Vertical walls in row 2
            (0,0,1,0,0,0), #Horizontal walls between rows 2&3
            (3,1,0,1,0,0,1,1), #Vertical walls in row 3
            (1,0,1,1,0,1), #Horizontal walls between rows 3&4
            (5,1,1,0,1,1,0,1), #Vertical walls in row 4
            (0,0,0,0,1,0), #Horizontal walls between rows 4&5
            (5,1,1,0,1,0,1,1), #Vertical walls in row 5
            (0,1,1,0,0,0), #Horizontal walls between rows 5&6
            (3,1,0,0,1,0,1,1), #Vertical walls in row 6
            (1,1,1,1,1,1)) #Bottom row of horizontal walls

#Corresponds to Instance2 Image
#6x6 Hard
instance2 = ((5,4,3,2,5,3),
            (1,1,1,1,1,1),
            (5,1,1,0,1,1,0,1),
            (0,1,1,0,1,1),
            (1,1,1,0,1,1,0,1),
            (1,1,1,1,1,1),
            (4,1,0,1,0,1,1,1),
            (1,1,1,1,1,0),
            (3,1,0,1,1,0,1,1),
            (0,0,1,1,1,1),
            (4,1,0,1,1,1,1,1),
            (1,1,0,1,0,0),
            (5,1,0,1,1,0,1,1),
            (1,1,1,1,1,1))

#Corresponds to Instance 3 Image
#6x6 Easy
instance3 = ((5,4,4,2,3,1),
            (1,1,1,1,1,1),
            (2,1,1,0,0,1,0,1),
            (0,0,0,0,1,1),
            (1,1,1,0,0,0,0,1),
            (0,0,0,1,1,1),
            (4,1,1,0,1,1,0,1),
            (0,1,1,0,1,0),
            (5,0,0,0,0,0,1,1),
            (1,0,1,1,0,0),
            (4,1,1,1,1,1,1,1),
            (0,1,0,0,1,0),
            (3,1,0,1,1,0,0,1),
            (1,1,1,1,1,1))

#Corresponds to Instance 4 Image
#15x15 Hard
instance4 = ((9,6,9,11,9,8,7,5,8,8,9,10,10,9,9),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
            (4,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1),
            (0,0,0,1,1,0,1,1,1,1,0,0,0,0,0),
            (7,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1),
            (0,1,1,0,1,1,1,1,1,0,1,1,0,1,1),
            (3,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1),
            (1,0,0,1,1,0,0,1,0,1,0,1,1,0,0),
            (4,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,1),
            (0,0,1,0,0,1,1,0,1,0,0,0,1,1,0),
            (10,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1),
            (1,1,0,0,1,1,1,1,0,0,0,1,0,0,0),
            (4,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1),
            (0,1,0,1,0,1,1,1,1,0,1,1,1,1,1),
            (11,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1),
            (1,1,1,1,0,0,0,1,0,1,1,1,0,1,1),
            (10,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1),
            (0,1,0,1,1,1,0,0,1,1,1,1,1,1,0),
            (6,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1),
            (1,0,0,0,1,0,1,1,0,1,0,1,1,0,1),
            (9,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1),
            (0,1,1,0,0,1,0,0,0,1,1,1,0,1,0),
            (9,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1),
            (0,0,1,1,0,1,0,0,1,1,1,0,1,0,0),
            (12,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1),
            (1,0,1,1,0,0,1,1,1,0,1,1,1,1,0),
            (13,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1),
            (0,0,0,1,1,0,0,1,0,1,1,1,1,1,0),
            (14,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1),
            (1,1,1,0,1,1,1,0,1,1,1,1,1,0,1),
            (11,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))

# Change this assignment to correspond to the instance desired
instance = instance4

# Although all Aquarium game boards are square, this code generalizes
# to any rectangular game board
height = int((len(instance) -2) /2)
width = len(instance[0])

# Creates an array of integer variables the size of the game board
# Represents the solution to the game board
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(width) ] for i in range(height) ]

# Ensures each cell is either a 1 or a 0 (filled or empty)
cells_c = [ Or(0 == X[i][j], X[i][j] == 1) for i in range(height) for j in range(width) ]

# Ensures each row has exactly the number of cells filled as the number dictated by
# the first number in that row
rows_c = [ Sum(X[i]) == instance[2*i+2][0] for i in range(height) ]

# Ensures each column has exactly the number of cells filled as the number dictated by
# the first number in that column
cols_c = [ (Sum([ X[i][j] for i in range(height) ]) == instance[0][j]) for j in range(width) ]

# Ensures each filled cell either has a wall below it or a filled cell below it
# Preserves the depth propert of aquariums (no floating water allowed)
depth_c = [ Or(X[i][j] == 0, instance[2*i+3][j] == 1, X[i+1][j] == 1) for i in range(height-1) for j in range(width) ]


# Returns whether there is a path between the given x,y coordinates
def path_between(from_x, from_y, to_x, to_y):
    worklist = [[from_x, from_y]]
    seen = []
    while (len(worklist) > 0):
        curr = worklist.pop()
        curr_x = curr[0]
        curr_y = curr[1]
        if (curr_x == to_x and curr_y == to_y):
            return True
        elif (not (curr in seen)):
            if (instance[2*curr_x + 2][curr_y + 2] == 0):
                worklist.append([curr_x, curr_y + 1])
            if (instance[2*curr_x + 2][curr_y + 1] == 0):
                worklist.append([curr_x, curr_y - 1])
            if (instance[2*curr_x + 1][curr_y] == 0):
                worklist.append([curr_x - 1, curr_y])
            if (instance[2*curr_x + 3][curr_y] == 0):
                worklist.append([curr_x + 1, curr_y])
        seen.append(curr)
    return False

# Ensures that at each level of an aquarium, water level is constant, even if cells aren't
# directly connected. As long as the two cells are on the same level and in the same aquarium
# they should both have the same fill status
aquarium_level_constant_c = [If(And(X[i][j] == 1, path_between(i,j,i,k)), X[i][k] == 1, True)
                           for i in range(height) for j in range(width) for k in range(width)]

# Collection of all restraints on the puzzle
puzzle_c = cells_c + rows_c + cols_c + depth_c + aquarium_level_constant_c

# Creates a new solver instance, adds the restraints, and attempts to solve the puzzle
s = Solver()
s.add(puzzle_c)
# To see all constraints written out, uncomment the next line
# print(s.to_smt2())
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(width) ] for i in range(height) ]
    print_matrix(r)
else:
    print("failed to solve")
