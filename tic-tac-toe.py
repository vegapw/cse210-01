# Tic-Tac-Toe assignment
# Author: Fredy Vega

# Main function
def main():
    the_end = False
    draw = False
    counter = 1
    mark_number = 0
    number_coordinates = [0,0]
    initial_grid = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]
    paint_board(initial_grid)
    
    while ((not the_end) and (counter < 10)):

        if (counter % 2 != 0):
            mark_number = choose_a_square("x", initial_grid)
            get_position(mark_number,number_coordinates)
            mark_position(initial_grid, number_coordinates, "x")
        else:
            mark_number = choose_a_square("o", initial_grid)
            get_position(mark_number,number_coordinates)
            mark_position(initial_grid, number_coordinates, "o")
        the_end = has_winner(initial_grid)
        draw = check_draw(initial_grid)
        if the_end:
            if (counter % 2 != 0):
                print(f"Game over, player of x's won")
            else:
                print(f"Game over, player of o's won")
        else:
            if draw:
                print("Game over, we have a draw!!")
            else:
                paint_board(initial_grid)
                counter += 1


# This function prints the board of tic-tac-toe
def paint_board(board):
    for i in range(3):
        for j in range(3):
            print(f"{board[i][j]}", end="")
            if j != 2:
                print("|",end="")
        print("\n-+-+-")

# This function ask and validates if the number is correct and 
# if the position in the board already have an "x" or "o"
def choose_a_square(letter, board):
    number = -1
    list = [0,0]
    while (number<1 or number>9) :
        number = int(input(f"{letter}'s turn to choose a square (1-9): "))
        if (number<1 or number>9):
            print("Wrong number!!, try again!!")
        else:
            get_position(number,list)
            if (board[list[0]][list[1]] in ["x","o"]):
                print("Wrong number!!, try again!!")
                number = -1
    return number

def mark_position(board, coordinate, letter):
    board[coordinate[0]][coordinate[1]] = letter

def get_position(number, coordinate):
    position = [
        [1, 0, 0],
        [2, 0, 1],
        [3, 0, 2],
        [4, 1, 0],
        [5, 1, 1],
        [6, 1, 2],
        [7, 2, 0],
        [8, 2, 1],
        [9, 2, 2]
    ]
    for i in range(9):
        if (position[i][0] == number):
            coordinate[0] = position[i][1] 
            coordinate[1] = position[i][2]


def has_winner(board):
    return (board[0][0] == board[0][1] == board[0][2] or
            board[1][0] == board[1][1] == board[1][2] or
            board[2][0] == board[2][1] == board[2][2] or
            board[0][0] == board[1][1] == board[2][2] or
            board[0][0] == board[1][0] == board[2][0] or
            board[0][1] == board[1][1] == board[2][1] or
            board[0][2] == board[1][2] == board[2][2] or
            board[2][0] == board[1][1] == board[0][2])

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != "x" and board[i][j] != "o":
                print(f"current value: {board[i][j]}")
                return False
    return True


# If this file was executed like this:
# > python tic-tac-toe.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()