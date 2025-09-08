def main():
    
    while True:
        try:
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
    for col in length:
        try:
            length.remove(grid[row][col])
        except ValueError:
            pass
    return length



main()