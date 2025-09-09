import math
def main():
    
    while True:
        try:
            #get side length, until enters a valid value
            sideL = int(input("Side length: "))
            break
        except ValueError:
            pass
    startGrid, unknownList = startingGrid(sideL)
    for row in startGrid:

        print(row)
    for row in unknownList:
        print(row)

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
                        unknown.append([i,inputRow.index(e, a)])
                    if not e.isalnum:
                        break
                    a += 1
                break
            else:
                print("Row is not equivalent to side length")
        
        grid.append(inputRow)
    return grid, unknown

def guessRow(grid, row, length):
    #removes values that are in the row, by iterating through each column
    for col in length:
        try:
            length.remove(grid[row][col])
        except ValueError:
            pass
    return length

def guessCol(grid, col, length):
    #removes values that are in the column, by iterating through each row
    for row in length:
        try:
            length.remove(grid[row][col])
        except ValueError:
            pass
    return length

def guessGrid(grid, position, length):
    gridLength = math.sqrt(len(length))
    (position[0]+1)%gridLength



main()