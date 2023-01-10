'''
Author: Tanner Barcus
Date: 11/10/2022
Purpose: Solve sudoku puzzle suing depth first search recursion from input file.
'''

file_name = input("Input file: ")       #request file from user

file = open(file_name)                  #open file
board = []                              #new list for board

for line in file:                       #iterate through file
    char = line.split()                 #slpit each line into a list
    board.append(char)                  #add list to board

print()                                 #print blank line
for line in board:                      #iterate through board
    print(*line)                        #print line in format


'''possible_move checks if the next move to make is valid.'''


def possible_move(x, y, val, board):                                    #creates new function
    for index in range(0, 9):                                           #iterates through 0-9 nums
        if board[y][index] == val:                                      #check if that num at that index is the value
            return False                                                #if it is return false
    for index in range(0, 9):                                           #iterates through 0-9 nums
        if board[index][x] == val:                                      #checks if that num at that index is the value
            return False                                                #if it is return false
    x_in_square = (x//3)*3                                              #create value for checking in 3x3 square
    y_in_square = (y//3)*3                                              #create value for checking in 3x3 square
    for index in range(0, 3):                                           #iterate through 0-3
        for i in range(0, 3):                                           #iterate through 0-3
            if board[y_in_square + index][x_in_square + i] == val:      #apply previous defined boundaries for 3x3 square and cheks if value is in it
                return False                                            #if it is return false
    return True                                                         #if no conditions apply return true


'''is_solved checks all spots for an '_' and if one remains returns false, otherwise returns true.'''


def is_solved(board):                   #create new function
    for x in range(9):                  #iterate through range 9
        for y in range(9):              #iterate through range 9
            if board[y][x] == "_":      #if any val at any coordinate in list is '_'
                return False            #return false
    return True                         #otherwise return true


'''solver checks if the puzzle is solved, then takes a number and places it at a valid move and then calls itself.'''


def solver(board):                                                  #create new function
    if is_solved(board):                                            #checks if is_solved is true or false
        for line in board:                                          #if it is prints board
            print(*line)                                            #print in format
        return True                                                 #return true
    for y in range(9):                                              #gets num in range 9 for y coordinate
        for x in range(9):                                          #gets num in range 9 for x coordinate
            if board[y][x] == "_":                                  #if at x and y the val is '_'
                for val in range(1, 10):                            #get val to place 1-10
                    if possible_move(x, y, str(val), board):        #if possible_move is true
                        board[y][x] = str(val)                      #place that val at the location
                        if solver(board):                           #if solver is true from before
                            return True                             #also return true
                    board[y][x] = "_"                               #if not place the val back at '-'
                return False                                        #return False


print()                             #print blank line
print("Puzzle Solution:", "\n")     #print header
if not solver(board):               #run solver and if not true
    print("No solution")            #print no solution
