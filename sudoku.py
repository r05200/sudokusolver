import math
import sudokuclass
import copy

def main():
    solved = sudoku_solver()
    for row in solved:
        print(row)

def sudoku_solver(starting_grid=None, side_length=None):
    # start_grid, unknown_list, side_l = set_state_before_solve()

    #receives the starting grid formatted into an array (start_grid), and also receives the position of each unknown
    # start_grid, unknown_list = starting_grid(side_l)
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
    
    
    
    if starting_grid is not None:
        start_grid = starting_grid
    else:
        # start_grid = [
        #     ['2', '4', '3', '1'],
        #     ['3', '1', '4', '2'],
        #     ['1', '3', '2', '4'],
        #     ['4', '2', '1', '3']
        # ]

        start_grid = [
            ['a', '2', 'b', '4', '5', '6', 'c', '8', '9', '10', '11', 'd', '13', 'e', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'f', '25'],
                ['6', 'c', 'g', '9', '10', '11', 'd', '13', '14', 'h', '16', 'i', '18', 'j', '20', 'k', '22', 'l', 'f', '25', '1', 'm', 'b', '4', 'n'],
                ['o', 'd', 'p', 'e', '15', '16', 'i', '18', '19', 'q', 'k', 'r', 'l', 'f', 's', '1', 'm', '3', '4', '5', 't', 'c', '8', 'u', 'v'],
                ['w', 'i', 'x', '19', 'q', '21', '22', 'l', 'f', '25', 'a', '2', '3', 'y', '5', 't', '7', 'g', 'u', '10', 'o', 'd', 'p', '14', 'h'],
                ['21', '22', '23', '24', '25', 'a', 'm', '3', '4', '5', '6', '7', '8', '9', 'v', '11', '12', '13', 'e', 'h', 'w', '17', '18', '19', '20'],
                ['2', 'b', '4', '5', 't', '7', '8', 'u', 'v', 'o', 'd', 'p', '14', '15', '16', '17', '18', 'j', '20', 'k', '22', '23', 'f', '25', '1'],
                ['7', '8', 'u', '10', 'o', 'd', '13', '14', '15', 'w', '17', '18', '19', 'q', '21', '22', '23', '24', 's', '1', 'm', '3', 'y', '5', 't'],
                ['d', '13', 'e', '15', '16', '17', '18', 'j', 'q', 'k', 'r', 'l', 'f', '25', 'a', '2', '3', 'y', '5', 't', '7', '8', '9', '10', '11'],
                ['i', 'x', '19', 'q', 'k', 'r', '23', '24', '25', '1', 'm', '3', 'y', '5', 't', '7', '8', '9', '10', 'o', 'd', '13', '14', 'h', '16'],
                ['r', 'l', '24', 's', '1', '2', '3', '4', 'n', '6', '7', '8', '9', 'v', '11', '12', '13', 'e', '15', '16', 'i', 'x', 'j', 'q', 'k'],
                ['3', '4', '5', 't', 'c', '8', '9', 'v', '11', '12', '13', '14', '15', 'w', 'i', 'x', '19', '20', '21', '22', 'l', '24', 's', 'a', 'm'],
                ['8', 'u', 'v', 'o', '12', '13', 'e', '15', '16', '17', '18', 'j', '20', '21', 'r', 'l', 'f', '25', '1', 'm', '3', 'y', '5', '6', '7'],
                ['13', 'e', '15', '16', '17', '18', 'j', 'q', 'k', '22', '23', '24', 's', '1', 'm', 'b', 'y', 'n', '6', '7', '8', 'u', '10', '11', 'd'],
                ['18', '19', '20', '21', 'r', '23', 'f', '25', '1', '2', 'b', '4', 'n', '6', '7', '8', '9', '10', '11', '12', '13', 'e', '15', 'w', 'i'],
                ['l', 'f', '25', 'a', 'm', 'b', 'y', '5', 't', '7', '8', 'u', '10', 'o', '12', '13', '14', '15', '16', '17', 'x', '19', '20', '21', 'r'],
                ['4', '5', '6', 'c', 'g', '9', 'v', '11', 'd', '13', '14', '15', '16', 'i', '18', '19', '20', '21', '22', '23', 'f', 's', '1', '2', 'b'],
                ['u', '10', '11', '12', 'p', '14', 'h', 'w', 'i', '18', '19', 'q', 'k', '22', '23', '24', '25', '1', '2', 'b', '4', '5', '6', '7', '8'],
                ['e', '15', '16', 'i', 'x', 'j', 'q', '21', '22', 'l', '24', 's', 'a', '2', 'b', '4', '5', 't', 'c', 'g', 'u', '10', 'o', 'd', '13'],
                ['19', '20', 'k', '22', '23', '24', 's', '1', '2', 'b', 'y', '5', '6', '7', 'g', '9', '10', 'o', '12', '13', 'e', '15', 'w', '17', '18'],
                ['24', 's', '1', '2', '3', '4', '5', '6', '7', '8', 'u', '10', '11', '12', '13', 'e', '15', '16', 'i', 'x', 'j', '20', '21', '22', '23'],
                ['n', '6', '7', '8', '9', 'v', 'o', '12', 'p', 'e', 'h', '16', '17', '18', 'j', 'q', '21', '22', '23', 'f', '25', '1', '2', '3', 'y'],
                ['10', '11', '12', '13', '14', '15', '16', '17', '18', 'j', '20', '21', 'r', '23', 'f', '25', 'a', '2', 'b', 'y', '5', '6', '7', 'g', '9'],
                ['15', 'w', 'i', 'x', '19', 'q', 'k', 'r', '23', '24', 's', 'a', 'm', 'b', 'y', '5', '6', '7', '8', '9', 'v', '11', '12', 'p', '14'],
                ['20', 'k', '22', '23', 'f', 's', 'a', 'm', 'b', 'y', '5', 't', 'c', '8', 'u', 'v', '11', 'd', '13', '14', '15', 'w', '17', '18', '19'],
                ['25', '1', '2', 'b', '4', '5', '6', 'c', '8', 'u', '10', '11', '12', '13', '14', 'h', 'w', '17', '18', '19', 'q', '21', '22', '23', '24']
        ]
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
    unknown_list = debug_start_grid(start_grid)
    if len(unknown_list) == 0:
        return start_grid
    
    if side_length is not None:
        side_l = side_length
    else:
        side_l = 25
    #for each unknown, it takes out the values that are already in its row/column/box
    sorted_unknowns = get_possible(unknown_list, start_grid, side_l)
    if len(sorted_unknowns[0]["possible"]) == 0:
        return "cannot solve grid" 
    # print(sorted_unknowns)
    solved = solve_sudoku(start_grid, sorted_unknowns)
    return solved


def starting_grid(l):
    grid = []
    unknown = []
    print("Input the rows of the grid, separating each number with a space. Use letters for unknowns.")
    #iterates through each number, so each row out of the total
    for i in range(l):
        while True:
            input_row = input("Input row: ").split(" ")
            if len(input_row) == l:
                
                for index, inputs in enumerate(input_row):
                    if inputs.isalpha():
                        #appends positions of all unknowns to unknownlist, starting from index a to prevent duplicate letters
                        unknown.append([i,input_row.index(inputs, index)])
                    if not inputs.isalnum:
                        break
                break
            else:
                print("Row is not equivalent to side length")
    #puts row in list, to form the starting grid
        grid.append(input_row)
    return grid, unknown

def set_state_before_solve():
    while True:
        try:
            #get side length, until enters a valid value
            side_l = int(input("Side length: "))
            break
        except ValueError:
            pass
    grid, unknowns = starting_grid(side_l)
    return grid, unknowns, side_l
    

def debug_start_grid(grid):
    unknown = []
    for index, row in enumerate(grid):

        for idx, item in enumerate(row):
            if item.isalpha():
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


def generate_layer(start_node, sorted_list):
    # print("iteration at depth: " + str(start_node.get_depth()))
    # print(start_node.grid)
    # if len(sorted_list) == 0:
    #         print("returned finished grid")
    #         print(start_node.grid)
    #         return start_node.grid 
    # print("sorted_list length: " + str(len(sorted_list)))
    # for s in sorted_list:
    #     print(s)
    # for item in sorted_list:
    #     if item["position"] in [[1, 1], [2, 1]]:
    #         print("below is the item ")
    #         print(item)
    #TEMP FIX BECAUSE IT BACKTRACKS AND IF NOT COPIED IT WILL SAY IT IS 0 AND SHOW AN ERROR, NEED TO FIGURE OUT WHY IT EVEN REPEATS
    # copied_list = copy.deepcopy(sorted_list)
    current_unknown = sorted_list.pop(0)
    if current_unknown["possible"] == []:
        return None
    #removes first entry in order to pass the updated list to the next level
    # print("popped list")
    
    #generates a new child for each possible number
    # print("possible:", current_unknown["possible"])
    for idx, possible in enumerate(current_unknown["possible"]):
        #deepcopies in order to separate the objects once they are edited through possible ande dependencies
        new_list = copy.deepcopy(sorted_list)
        # print(new_list)
        # print("deepcopied list")
        #generates a new deepcopied grid from the original to edit
        new_grid = copy.deepcopy(start_node.grid)
        # print("deepcopied grid")
        #sets the unknown as the tried value
        new_grid[current_unknown["position"][0]][current_unknown["position"][1]] = str(possible)
        # print("added value to new grid" + str(possible))
        # print("this is grid " + str(idx) + " of depth " + str(start_node.get_depth() + 1))
        # print(new_grid)
        
        #iterates through all the possibilities in new_list, and if it is inside the current selected unknown's dependency list, removes possible from their possible list
        if len(new_list) >= 1:
            min_length = len(new_list[0]["possible"])
            for idx, unknown in enumerate(new_list):
                if unknown["position"] in current_unknown["dependencies"]:
                    try:
                        # print("removed: " + str(possible))
                        unknown["possible"].remove(possible)
                    except:
                        # print("passed removal")
                        pass
                    if len(unknown["possible"]) == 0:
                        return None
                    if len(unknown["possible"]) < min_length:
                        shortest = new_list.pop(idx)
                        new_list.insert(0, shortest)
        if len(new_list) != 0:
            child_node = sudokuclass.GameState(new_grid)
            start_node.add_children(child_node)
            # print("below is number of children")
            # print(len(start_node.children))
            # print("generating layer at depth " + str(child_node.get_depth()))
            result = generate_layer(child_node, new_list)
            if result is not None:
                # print("generating layer at depth " + str(child_node.get_depth()))
                
                return result
            else: 
                # print("continued")
                continue
        else:
            # print("length is 0 for new list")
            return new_grid


def solve_sudoku(start_grid, sorted_unknowns):
    initial_node = sudokuclass.GameState(start_grid)
   
    solved = generate_layer(initial_node, sorted_unknowns)
    return solved

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