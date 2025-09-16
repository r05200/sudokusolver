import math
import sys
def main():
    sortedUnknowns = []
    unknown = {}
    while True:
        try:
            #get side length, until enters a valid value
            sideL = int(input("Side length: "))
            
            break
        except ValueError:
            pass
    startGrid, unknownList = startingGrid(sideL)
    
    print(unknownList)
    for pos in unknownList:
    
        guessList = list(range(1,sideL+1))
        p = checkCol(startGrid, pos[1], sideL, guessList)
        t = checkRow(startGrid, pos[0], sideL, p)
        z = checkBox(startGrid, pos, sideL, t)
        print(z)
        sortedUnknowns.append([pos, z])



def startingGrid(l):
    grid = []
    unknown = []

    #iterates through each number, so each row out of the total
    for i in range(l):
        while True:
            inputRow = input("Input row: ").split(" ")
            if len(inputRow) == l:
                a = 0
                for e in inputRow:
                    if e.isalpha():
                        #appends positions of all unknowns to unknownlist
                        unknown.append([i,inputRow.index(e, a)])
                    if not e.isalnum:
                        break
                    a += 1
                break
            else:
                print("Row is not equivalent to side length")
    #puts row in list, to form the starting grid
        grid.append(inputRow)
    return grid, unknown

def checkRow(grid, row, sideLen, possible):
    #removes values that are in the row, by iterating through each column
    for col in list(range(sideLen)):
        try:
            possible.remove(int(grid[row][col]))
            #print("removed" + str(grid[row][col]))
        except ValueError:
            pass
    return possible

def checkCol(grid, col, sideLen, possible):
    #removes values that are in the column, by iterating through each row
    for row in list(range(sideLen)):
        try:
            possible.remove(int(grid[row][col]))
            #print("removed" + str(grid[row][col]))
        except ValueError:
            pass
    return possible

def checkBox(grid, position, sideLen, possible):
    boxLength = math.sqrt(sideLen)
    boxLeftBound = int(position[1] - (int(position[1]))%boxLength)
    boxUpperBound = int(position[0] - int(position[0])%boxLength)
    for entry in range(boxUpperBound, int(boxUpperBound + boxLength)):
        for entry2 in range(boxLeftBound, int(boxLeftBound + boxLength)):
            try:
                possible.remove(int(grid[entry][entry2]))
            except ValueError:
                pass
    return possible


main()

#test sudoku 2x2
# 2 4 3 1       x 4 t 1    expected: (2, 4), (2, 3), (2, 3), (2, 3)
# 3 1 4 2       3 1 4 d    expected: (2), (2)
# 1 3 2 4       1 c v 4    expected: (2, 3), (3), (2, 3), (2, 3)
# 4 2 1 3       x 2 1 3    expected: (2, 4), (4)
