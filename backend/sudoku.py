import math
import sudokuclass as sudokuclass
from random import randint

def main():
    solved = sudoku_solver()
    for row in solved:
        print(row)
    # puzzle = sudoku_generator(9, 25)
    # for row in puzzle:
    #     print(row)



def sudoku_solver(starting_grid=None, side_length=None):
    # start_grid, unknown_list, side_l = set_state_before_solve()

    #receives the starting grid formatted into an array (start_grid), and also receives the position of each unknown
    # start_grid, unknown_list = starting_grid(side_l)

    print(starting_grid)
    if starting_grid is not None:
        start_grid = starting_grid
    else:
        #     start_grid = [
#   ["4", "z", "x", "c", "v", "5", "8", "6", "b"],
#   ["n", "m", "1", "a", "s", "4", "d", "2", "f"],
#   ["7", "g", "h", "3", "2", "j", "k", "4", "5"],
#   ["1", "q", "5", "w", "9", "r", "t", "7", "y"],
#   ["u", "i", "8", "1", "o", "6", "9", "p", "z"],
#   ["x", "6", "c", "v", "8", "b", "3", "n", "4"],
#   ["9", "5", "m", "a", "3", "1", "s", "d", "6"],
#   ["f", "3", "g", "8", "h", "j", "5", "k", "l"],
#   ["q", "1", "2", "6", "w", "e", "r", "t", "7"]
# ]
    
    #For debug, adding test case
        # start_grid = [
        
        #     ['x', 'c', 'h', 'g'],
        #     ['4', 'f', 's', 'd'],
        #     ['x', '1', '4', '3'],
        #     ['3', '4', 'k', 'r']
        # ]
        # start_grid = [
        #     ['x', 'f', '3', '1'],
        #     ['c', '1', 'n', '2'],
        #     ['1', '3', '2', '4'],
        #     ['4', 'j', '1', '3']
        # ]

        # start_grid = [
        #     ['2', '4', '3', '1'],
        #     ['3', '1', '4', '2'],
        #     ['1', '3', '2', '4'],
        #     ['4', '2', '1', '3']
        # ]

        # 
        start_grid = [
            ['x', 'u', 't', '1'],
            ['3', 'l', '4', 'd'],
            ['1', 'c', 'v', '4'],
            ['x', 'j', 'f', 'y']
        ]
        # start_grid = [
        #     ['a', 'b', '3', '4', '5', 'l', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'],
        #     ['6', '7', '8', '9', '10', 'm', 'i', 'n', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5'],
        #     ['f', 'e', '13', '14', '15', 'g', 'h', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        #     ['16', 'd', '18', '19', '20', 'j', 'k', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
        #     ['21', 'c', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
        #     ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1'],
        #     ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6'],
        #     ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
        #     ['17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'],
        #     ['22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
        #     ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2'],
        #     ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7'],
        #     ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        #     ['18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'],
        #     ['23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'],
        #     ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3'],
        #     ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8'],
        #     ['14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
        #     ['19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
        #     ['24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
        #     ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4'],
        #     ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        #     ['15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
        #     ['20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
        #     ['25', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        # ]
        # start_grid = [
        #     ['9', 'm', 'l', 'q', 'i', '17', '4', '14', 'w', 'g', 'j', 's', 'v', 't', 'h', 'n', '11', '24', '25', 'p', 'u', '2', '13', 'f', '3'],
        #     ['j', 't', 'v', 's', 'h', 'p', 'n', '24', '25', '11', '3', 'u', '13', 'f', '2', 'i', 'l', 'm', 'q', '9', 'w', '4', 'g', '14', '17'],
        #     ['17', '14', 'g', 'w', '4', 'j', 'h', 't', 's', 'v', 'p', '25', '11', '24', 'n', '2', '13', 'f', 'u', '3', 'q', 'i', 'l', 'm', '9'],
        #     ['p', '24', '11', '25', 'n', '3', '2', 'f', 'u', '13', '9', 'q', 'l', 'm', 'i', '4', 'g', '14', 'w', '17', 's', 'h', 'v', 't', 'j'],
        #     ['3', 'f', '13', 'u', '2', '9', 'i', 'm', 'q', 'l', '17', 'w', 'g', '14', '4', 'h', 'v', 't', 's', 'j', '25', 'n', '11', '24', 'p'],
        #     ['q', 'h', 'j', 'm', 'l', 'w', 'g', 'n', '14', 'p', 's', 't', '3', '2', 'v', '11', '9', 'i', '24', '25', 'f', '13', '17', '4', 'u'],
        #     ['u', '4', '17', 'f', '13', 'q', 'l', 'h', 'm', 'j', 'w', '14', 'p', 'n', 'g', 'v', '3', '2', 't', 's', '24', '11', '9', 'i', '25'],
        #     ['s', '2', '3', 't', 'v', '25', '11', 'i', '24', '9', 'u', 'f', '17', '4', '13', 'l', 'j', 'h', 'm', 'q', '14', 'g', 'p', 'n', 'w'],
        #     ['w', 'n', 'p', '14', 'g', 's', 'v', '2', 't', '3', '25', '24', '9', 'i', '11', '13', '17', '4', 'f', 'u', 'm', 'l', 'j', 'h', 'q'],
        #     ['25', 'i', '9', '24', '11', 'u', '13', '4', 'f', '17', 'q', 'm', 'j', 'h', 'l', 'g', 'p', 'n', '14', 'w', 't', 'v', '3', '2', 's'],
        #     ['2', '17', 'f', '13', 'u', 'i', 'q', 'j', 'l', 'm', '4', 'g', '14', 'p', 'w', 's', 't', '3', 'v', 'h', '11', '25', '24', '9', 'n'],
        #     ['h', '3', 't', 'v', 's', 'n', '25', '9', '11', '24', '2', '13', 'f', '17', 'u', 'q', 'm', 'j', 'l', 'i', 'g', 'w', '14', 'p', '4'],
        #     ['i', 'j', 'm', 'l', 'q', '4', 'w', 'p', 'g', '14', 'h', 'v', 't', '3', 's', '25', '24', '9', '11', 'n', '13', 'u', 'f', '17', '2'],
        #     ['n', '9', '24', '11', '25', '2', 'u', '17', '13', 'f', 'i', 'l', 'm', 'j', 'q', 'w', '14', 'p', 'g', '4', 'v', 's', 't', '3', 'h'],
        #     ['4', 'p', '14', 'g', 'w', 'h', 's', '3', 'v', 't', 'n', '11', '24', '9', '25', 'u', 'f', '17', '13', '2', 'l', 'q', 'm', 'j', 'i'],
        #     ['14', '11', '25', 'n', 'p', 't', '3', '13', '2', 'u', '24', 'i', 'q', 'l', '9', '17', 'w', 'g', '4', 'f', 'h', 'j', 's', 'v', 'm'],
        #     ['24', 'l', 'q', 'i', '9', 'f', '17', 'g', '4', 'w', 'm', 'h', 's', 'v', 'j', 'p', '25', '11', 'n', '14', '2', '3', 'u', '13', 't'],
        #     ['m', 'v', 's', 'h', 'j', '14', 'p', '11', 'n', '25', 't', '2', 'u', '13', '3', '9', 'q', 'l', 'i', '24', '4', '17', 'w', 'g', 'f'],
        #     ['f', 'g', 'w', '4', '17', 'm', 'j', 'v', 'h', 's', '14', 'n', '25', '11', 'p', '3', 'u', '13', '2', 't', 'i', '9', 'q', 'l', '24'],
        #     ['t', '13', 'u', '2', '3', '24', '9', 'l', 'i', 'q', 'f', '4', 'w', 'g', '17', 'j', 's', 'v', 'h', 'm', 'n', 'p', '25', '11', '14'],
        #     ['v', 'u', '2', '3', 't', '11', '24', 'q', '9', 'i', '13', '17', '4', 'w', 'f', 'm', 'h', 's', 'j', 'l', 'p', '14', 'n', '25', 'g'],
        #     ['13', 'w', '4', '17', 'f', 'l', 'm', 's', 'j', 'h', 'g', 'p', 'n', '25', '14', 't', '2', 'u', '3', 'v', '9', '24', 'i', 'q', '11'],
        #     ['g', '25', 'n', 'p', '14', 'v', 't', 'u', '3', '2', '11', '9', 'i', 'q', '24', 'f', '4', 'w', '17', '13', 'j', 'm', 'h', 's', 'l'],
        #     ['l', 's', 'h', 'j', 'm', 'g', '14', '25', 'p', 'n', 'v', '3', '2', 'u', 't', '24', 'i', 'q', '9', '11', '17', 'f', '4', 'w', '13'],
        #     ['11', 'q', 'i', '9', '24', '13', 'f', 'w', '17', '4', 'l', 'j', 'h', 's', 'm', '14', 'n', '25', 'p', 'g', '3', 't', '2', 'u', 'v']
        # ]
        # start_grid = [
        #     ['4', '2', '3', '7', '1', '5', '8', 'o', 'p'],
        #     ['5', '8', '1', '9', '6', '4', 'c', 'h', '3'],
        #     ['7', '9', '6', '3', '2', '8', 'e', 'r', '5'],
        #     ['1', '4', '5', '2', '9', '3', '6', '7', '8'],
        #     ['b', 'v', '8', '1', '4', '6', '9', '5', '2'],
        #     ['2', '6', '9', '5', '8', '7', '3', '1', '4'],
        #     ['9', '5', '7', '4', '3', '1', '2', '8', '6'],
        #     ['6', '3', '4', '8', '7', '2', '5', 'f', 'e'],
        #     ['8', '1', '2', '6', '5', '9', '4', '3', 'k']
        # ]
        
        # start_grid = [
        #     ['5','3','4','6','7','8','9','1','2'],
        #     ['6','7','2','1','9','5','3','4','8'],
        #     ['1','9','8','3','4','2','5','6','7'],
        #     ['8','5','9','7','6','1','4','2','3'],
        #     ['f','n','6','8','5','3','7','9','1'],
        #     ['7','1','3','9','2','4','8','5','6'],
        #     ['9','6','1','5','3','7','2','8','4'],
        #     ['x','8','7','4','1','9','6','e','5'],
        #     ['t','a','5','2','8','6','1','7','9']
        # ]
        # start_grid = [
        #     ['9', '12', '10', '18', '7', '17', '4', '14', 'w', 'g', 'j', 's', 'v', 't', 'h', 'n', '11', '24', '25', 'p', 'u', '2', '13', 'f', '3'],
        #     ['8', '20', '22', '19', '6', 'p', 'n', '24', '25', '11', '3', 'u', '13', 'f', '2', 'i', 'l', 'm', 'q', '9', 'w', '4', 'g', '14', '17'],
        #     ['17', '14', 'g', 'w', '4', 'j', 'h', 't', 's', 'v', 'p', '25', '11', '24', 'n', '2', '13', 'f', 'u', '3', 'q', 'i', 'l', 'm', '9'],
        #     ['p', '24', '11', '25', 'n', '3', '2', 'f', 'u', '13', '9', 'q', 'l', 'm', 'i', '4', 'g', '14', 'w', '17', 's', 'h', 'v', 't', 'j'],
        #     ['3', 'f', '13', 'u', '2', '9', 'i', 'm', 'q', 'l', '17', 'w', 'g', '14', '4', 'h', 'v', 't', 's', 'j', '25', 'n', '11', '24', 'p'],
        #     ['q', 'h', 'j', 'm', 'l', 'w', 'g', 'n', '14', 'p', 's', 't', '3', '2', 'v', '11', '9', 'i', '24', '25', 'f', '13', '17', '4', 'u'],
        #     ['u', '4', '17', 'f', '13', 'q', 'l', 'h', 'm', 'j', 'w', '14', 'p', 'n', 'g', 'v', '3', '2', 't', 's', '24', '11', '9', 'i', '25'],
        #     ['s', '2', '3', 't', 'v', '25', '11', 'i', '24', '9', 'u', 'f', '17', '4', '13', 'l', 'j', 'h', 'm', 'q', '14', 'g', 'p', 'n', 'w'],
        #     ['w', 'n', 'p', '14', 'g', 's', 'v', '2', 't', '3', '25', '24', '9', 'i', '11', '13', '17', '4', 'f', 'u', 'm', 'l', 'j', 'h', 'q'],
        #     ['25', 'i', '9', '24', '11', 'u', '13', '4', 'f', '17', 'q', 'm', 'j', 'h', 'l', 'g', 'p', 'n', '14', 'w', 't', 'v', '3', '2', 's'],
        #     ['2', '17', 'f', '13', 'u', 'i', 'q', 'j', 'l', 'm', '4', 'g', '14', 'p', 'w', 's', 't', '3', 'v', 'h', '11', '25', '24', '9', 'n'],
        #     ['h', '3', 't', 'v', 's', 'n', '25', '9', '11', '24', '2', '13', 'f', '17', 'u', 'q', 'm', 'j', 'l', 'i', 'g', 'w', '14', 'p', '4'],
        #     ['i', 'j', 'm', 'l', 'q', '4', 'w', 'p', 'g', '14', 'h', 'v', 't', '3', 's', '25', '24', '9', '11', 'n', '13', 'u', 'f', '17', '2'],
        #     ['n', '9', '24', '11', '25', '2', 'u', '17', '13', 'f', 'i', 'l', 'm', 'j', 'q', 'w', '14', 'p', 'g', '4', 'v', 's', 't', '3', 'h'],
        #     ['4', 'p', '14', 'g', 'w', 'h', 's', '3', 'v', 't', 'n', '11', '24', '9', '25', 'u', 'f', '17', '13', '2', 'l', 'q', 'm', 'j', 'i'],
        #     ['14', '11', '25', 'n', 'p', 't', '3', '13', '2', 'u', '24', 'i', 'q', 'l', '9', '17', 'w', 'g', '4', 'f', 'h', 'j', 's', 'v', 'm'],
        #     ['24', 'l', 'q', 'i', '9', 'f', '17', 'g', '4', 'w', 'm', 'h', 's', 'v', 'j', 'p', '25', '11', 'n', '14', '2', '3', 'u', '13', 't'],
        #     ['m', 'v', 's', 'h', 'j', '14', 'p', '11', 'n', '25', 't', '2', 'u', '13', '3', '9', 'q', 'l', 'i', '24', '4', '17', 'w', 'g', 'f'],
        #     ['f', 'g', 'w', '4', '17', 'm', 'j', 'v', 'h', 's', '14', 'n', '25', '11', 'p', '3', 'u', '13', '2', 't', 'i', '9', 'q', 'l', '24'],
        #     ['t', '13', 'u', '2', '3', '24', '9', 'l', 'i', 'q', 'f', '4', 'w', 'g', '17', 'j', 's', 'v', 'h', 'm', 'n', 'p', '25', '11', '14'],
        #     ['v', 'u', '2', '3', 't', '11', '24', 'q', '9', 'i', '13', '17', '4', 'w', 'f', 'm', 'h', 's', 'j', 'l', 'p', '14', 'n', '25', 'g'],
        #     ['13', 'w', '4', '17', 'f', 'l', 'm', 's', 'j', 'h', 'g', 'p', 'n', '25', '14', 't', '2', 'u', '3', 'v', '9', '24', 'i', 'q', '11'],
        #     ['g', '25', 'n', 'p', '14', 'v', 't', 'u', '3', '2', '11', '9', 'i', 'q', '24', 'f', '4', 'w', '17', '13', 'j', 'm', 'h', 's', 'l'],
        #     ['l', 's', 'h', 'j', 'm', 'g', '14', '25', 'p', 'n', 'v', '3', '2', 'u', 't', '24', 'i', 'q', '9', '11', '17', 'f', '4', 'w', '13'],
        #     ['11', 'q', 'i', '9', '24', '13', 'f', 'w', '17', '4', 'l', 'j', 'h', 's', 'm', '14', 'n', '25', 'p', 'g', '3', 't', '2', 'u', 'v']
        # ]

    unknown_list = start_unknowns(start_grid)
    if len(unknown_list) == 0:
        return start_grid
    
    if side_length is not None:
        side_l = side_length
    else:
        side_l = 4
    #for each unknown, it takes out the values that are already in its row/column/box
    sorted_unknowns = get_possible(unknown_list, start_grid, side_l)
    print("sorted unknowns")
    print(sorted_unknowns)
    if len(sorted_unknowns[0]["possible"]) == 0:
        return "cannot solve grid" 
    # print(sorted_unknowns)
    solved = solve_sudoku(sorted_unknowns, start_grid)
    return solved
    

def start_unknowns(grid):
    print("within function")
    print(grid)
    unknown = []
    for index, row in enumerate(grid):
        print(row)
        for idx, item in enumerate(row):
            if item == '':
                #appends positions of all unknowns to unknownlist, starting from index a to prevent duplicate letters
                unknown.append([index,row.index(item, idx)])
    return unknown

def get_possible(unknown_list, start_grid, l):

    temp_list = []

    for pos in unknown_list:
        guess_list = list(range(1,l+1))
        #checks all cols/rows/boxes and removes them from guessList
        # print(pos)
        z = check_all(start_grid, pos, l, guess_list)
        dependencies = []
        for position in unknown_list:
            if check_dependencies(pos, position, l) and pos != position:
                dependencies.append(position)
        #dictionary for properties of each unknown
        temp_list.append({
            "position": pos,
            "possible": z,
            "dependencies": dependencies
            })
    
   #sort the unknowns to arrange them from least to greatest possibilities
    temp_list.sort(key=lambda x: len(x["possible"]))
    
    return temp_list

def check_row(grid, row, side_len, possible):
    #removes values that are in the row, by iterating through each column
    for col in list(range(side_len)):
        try:
            possible.remove(int(grid[row][col]))
            # print("removed in check row" + str(grid[row][col]))
        except ValueError:
            pass
    return possible

def check_col(grid, col, side_len, possible):
    #removes values that are in the column, by iterating through each row
    for row in list(range(side_len)):
        try:
            possible.remove(int(grid[row][col]))
            # print("removed in check col with col" + str(row) + str(col)+ str(grid[row][col]))
        except ValueError:
            pass
    return possible

def check_box(grid, position, side_len, possible):
    #get box length
    box_length = math.sqrt(side_len)
    #determine left bound by subtracting the x by the modulo of boxlength, which moves it to the closest bound of the box
    box_left_bound = int(position[1] - (int(position[1]))%box_length)
    #determine upper bound using same thing
    box_upper_bound = int(position[0] - int(position[0])%box_length)
    #iterates through each entry in box
    for entry in range(box_upper_bound, int(box_upper_bound + box_length)):
        for entry2 in range(box_left_bound, int(box_left_bound + box_length)):
            try:
                #removes the entry from possible
                possible.remove(int(grid[entry][entry2]))
            except ValueError:
                pass
    return possible

#does all checks, rows, cols and boxes
def check_all(grid, pos, side_len, guess_list):
    p = check_col(grid, pos[1], side_len, guess_list)
    t = check_row(grid, pos[0], side_len, p)
    k = check_box(grid, pos, side_len, t)
    return k

#check whether the 2nd cell is dependent on the first, could be put after sorted_unknowns for more efficiency
def check_dependencies(pos1, pos2, side_l):
    if pos1[0] == pos2[0] or pos1[1] == pos2[1] or same_box(pos1, pos2, side_l):
        return True

def same_box(pos1, pos2, side_l):
    if (pos1[0]-pos1[0]%math.sqrt(side_l))/math.sqrt(side_l) == (pos2[0]-pos2[0]%math.sqrt(side_l))/math.sqrt(side_l) and (pos1[1]-pos1[1]%math.sqrt(side_l))/math.sqrt(side_l) == (pos2[1]-pos2[1]%math.sqrt(side_l))/math.sqrt(side_l):
        return True
    return False

def generate_layer(start_stack):
    top = start_stack.top
    sorted_list = top.next_array
    
    while len(sorted_list) > 0:
        print("iterated")
        top = start_stack.top
        sorted_list = top.next_array
        
        if len(sorted_list) == 0:
            return start_stack
        
        current_unknown = sorted_list[0]
        
        while len(current_unknown["possible"]) == 0:
            start_stack.pop()
            top_node = start_stack.top
            current_unknown = top_node.next_array[0]
            sorted_list = top_node.next_array
            
        
        possible_list = []
        for grid in sorted_list[1:]:
            possible_list.append(
                {
                    "position": grid["position"][:],
                    "possible": grid["possible"][:],
                    "dependencies": grid["dependencies"][:]
                }
            )
        
        #remove dependencies
        
        value = current_unknown["possible"][0]
        for dependency in current_unknown["dependencies"]:
            # if current_unknown["position"] == [0,0] or current_unknown["position"] == [0,6]:
                
            
            for possible in possible_list:
                
                if possible["position"] == dependency:
                    # if current_unknown["position"] == [0,0] or current_unknown["position"] == [0,6]:
                    
                    
                    try:
                        possible["possible"].remove(value)
                        # if current_unknown["position"] == [0,0] or current_unknown["position"] == [0,6]:
                        
                    except:
                        pass
        current_unknown["possible"].remove(value)
        # if current_unknown["position"] == [0,0] or current_unknown["position"] == [0,6]:
        possible_list.sort(key=lambda x: len(x["possible"]))
        start_stack.push(value=value, position=current_unknown["position"], next_array=possible_list)
    
    # while start_stack.size() != len(sorted_list):


    # if current_unknown["possible"] == []:
    #     start_stack.pop()
    # new_node = sudokuclass.CurrentlyTried(next_array=new_list[0]["possible"], value=current_unknown["possible"][0])
    # start_stack.push(new_node)
    # for 
    # for possibility in current_unknown["possible"]:
    #     for item in new_list:
    #         if item in current_unknown["dependencies"]:

        
    
    
def stack_to_fill(start_stack, grid):
    array = []
    current_node = start_stack.top
    while current_node.prev is not None:
        array.append({
            "value": current_node.value,
            "position": current_node.position
        })
        current_node = current_node.prev
    print(array)
    for pair in array[::-1]:
        position = pair["position"]
        grid[position[0]][position[1]] = str(pair["value"])
        print(grid[position[0]][position[1]])
    return grid

def solve_sudoku(sorted_unknowns, grid):
    start_stack = sudokuclass.GameState()   
    start_stack.push(next_array=sorted_unknowns)
    
    end_stack = generate_layer(start_stack)
    node = start_stack.top
    print("below is nodes")
    while node.prev is not None:
        print(node)
        print(node.position)
        node = node.prev
    solved = stack_to_fill(end_stack, grid)
    return solved

def sudoku_generator(side_l, unknown_number):
    grid = empty_grid_generator(side_length=side_l)
    unknowns = start_unknowns(grid)
    print(unknowns)
    sorted_unknowns = get_possible(unknowns, grid, side_l)
    print("this is unknowns")
    print(sorted_unknowns)
    start_grid = generate_sudoku(sorted_unknowns, unknown_number, grid)
    return start_grid

def empty_grid_generator(side_length=None):
    print(side_length)
    if side_length is None:
        side_len = 25
    else:
        side_len = side_length

    grid = []
    for i in range(side_len):
        grid.append([])
        for _ in range(side_len):
            grid[i].append('a')
    print(grid)
    return grid

def generate_sudoku(unknowns, unknown_num, grid):
    new_stack = sudokuclass.GameState()
    new_stack.push(next_array=unknowns)
    end_stack = generate_puzzle_layer(new_stack, unknown_num)
    solved = stack_to_fill(end_stack, grid)
    return solved

def generate_puzzle_layer(start_stack, unknown_number):
    top = start_stack.top
    sorted_list = top.next_array
    
    while len(sorted_list) > unknown_number:
        print("iterated")
        top = start_stack.top
        sorted_list = top.next_array
        
        if len(sorted_list) == unknown_number:
            return start_stack
        rand_remove = randint(0, len(sorted_list)-1)
        print(rand_remove)
        current_unknown = sorted_list[rand_remove]
        sorted_list[rand_remove] = sorted_list[0]
        sorted_list[0] = current_unknown
        
        
        while len(current_unknown["possible"]) == 0:
            start_stack.pop()
            top_node = start_stack.top
            current_unknown = top_node.next_array[0]
            sorted_list = top_node.next_array
            
        
        possible_list = []
        for grid in sorted_list[1:]:
            possible_list.append(
                {
                    "position": grid["position"][:],
                    "possible": grid["possible"][:],
                    "dependencies": grid["dependencies"][:]
                }
            )
        
        #remove dependencies
        rand = randint(0, len(current_unknown["possible"]) - 1)
        value = current_unknown["possible"][rand]
        for dependency in current_unknown["dependencies"]:
            # if current_unknown["position"] == [0,0] or current_unknown["position"] == [0,6]:
                
            
            for possible in possible_list:
                
                if possible["position"] == dependency:
                    try:
                        possible["possible"].remove(value)
                    except:
                        pass
        current_unknown["possible"].remove(value)
        
        possible_list.sort(key=lambda x: len(x["possible"]))
        start_stack.push(value=value, position=current_unknown["position"], next_array=possible_list)
    
    
if __name__ == "__main__":    
    main()

#test sudoku 2x2
# 2 4 3 1       x 4 t 1    expected: (2, 4), (2, 3), (2, 3), (2, 3)  possible per position: [2], [2,3]
# 3 1 4 2       3 1 4 d    expected: (2), (2)                        possible per position: [2,3]
# 1 3 2 4       1 c v 4    expected: (2, 3), (3), (2, 3), (2, 3)     possible per position: [3], [2,3]
# 4 2 1 3       x 2 1 y    expected: (2, 4), (4)                     possible per position: [4], [3]

#test sudoku 2x2

# 1 2 3 4   x c h g
# 4 3 1 2   4 f s d
# 2 1 4 3   x 1 4 3
# 3 4 2 1   3 4 k r

#test sudoku 9x9            solved
# 4 z x c v 5 8 6 b         4 2 3 7 1 5 8 6 9
# n m 1 a s 4 d 2 f         5 8 1 9 6 4 7 2 3
# 7 g h 3 2 j k 4 5         7 9 6 3 2 8 1 4 5
# 1 q 5 w 9 r t 7 y         1 4 5 2 9 3 6 7 8
# u i 8 1 o 6 9 p z         3 7 8 1 4 6 9 5 2 
# x 6 c v 8 b 3 n 4         2 6 9 5 8 7 3 1 4
# 9 5 m a 3 1 s d 6         9 5 7 4 3 1 2 8 6 
# f 3 g 8 h j 5 k l         6 3 4 8 7 2 5 9 1
# q 1 2 6 w e r t 7         8 1 2 6 5 9 4 3 7




# # print("iteration at depth: " + str(start_node.get_depth()))
#     # print(start_node.grid)
#     # if len(sorted_list) == 0:
#     #         print("returned finished grid")
#     #         print(start_node.grid)
#     #         return start_node.grid 
#     # print("sorted_list length: " + str(len(sorted_list)))
#     # for s in sorted_list:
#     #     print(s)
#     # for item in sorted_list:
#     #     if item["position"] in [[1, 1], [2, 1]]:
#     #         print("below is the item ")
#     #         print(item)
#     #TEMP FIX BECAUSE IT BACKTRACKS AND IF NOT COPIED IT WILL SAY IT IS 0 AND SHOW AN ERROR, NEED TO FIGURE OUT WHY IT EVEN REPEATS
#     # copied_list = copy.deepcopy(sorted_list)
#     current_unknown = sorted_list.pop(0)
#     if current_unknown["possible"] == []:
#         return None
#     #removes first entry in order to pass the updated list to the next level
#     # print("popped list")
    
#     #generates a new child for each possible number
#     # print("possible:", current_unknown["possible"])
#     for idx, possible in enumerate(current_unknown["possible"]):
#         #deepcopies in order to separate the objects once they are edited through possible ande dependencies
#         new_list = copy.deepcopy(sorted_list)
#         # print(new_list)
#         # print("deepcopied list")
#         #generates a new deepcopied grid from the original to edit
#         new_grid = copy.deepcopy(start_node.grid)
#         # print("deepcopied grid")
#         #sets the unknown as the tried value
#         new_grid[current_unknown["position"][0]][current_unknown["position"][1]] = str(possible)
#         # print("added value to new grid" + str(possible))
#         # print("this is grid " + str(idx) + " of depth " + str(start_node.get_depth() + 1))
#         # print(new_grid)
        
#         #iterates through all the possibilities in new_list, and if it is inside the current selected unknown's dependency list, removes possible from their possible list
#         if len(new_list) >= 1:
#             min_length = len(new_list[0]["possible"])
#             for idx, unknown in enumerate(new_list):
#                 if unknown["position"] in current_unknown["dependencies"]:
#                     try:
#                         # print("removed: " + str(possible))
#                         unknown["possible"].remove(possible)
#                     except:
#                         # print("passed removal")
#                         pass
#                     if len(unknown["possible"]) == 0:
#                         return None
#                     # if len(unknown["possible"]) < min_length:
#                     #     shortest = new_list.pop(idx)
#                     #     new_list.insert(0, shortest)
#                     new_list.sort(key=lambda x: len(x["possible"]))
#         if len(new_list) != 0:
#             child_node = sudokuclass.GameState(new_grid)
#             start_node.add_children(child_node)
#             # print("below is number of children")
#             # print(len(start_node.children))
#             # print("generating layer at depth " + str(child_node.get_depth()))
#             result = generate_layer(child_node, new_list)
#             if result is not None:
#                 # print("generating layer at depth " + str(child_node.get_depth()))
#                 print("here")
#                 return result
#             else: 
#                 # print("continued")
#                 continue
#         else:
#             # print("length is 0 for new list")
            
#             return new_grid
