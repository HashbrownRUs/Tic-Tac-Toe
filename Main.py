import sys, re
from itertools import cycle

GameOver = False
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
players = cycle(["X","O"]) 

def display_board(v1,v2,v3,v4,v5,v6,v7,v8,v9):

    print(
    """
        _ _ _ _ 
    2  | {} {} {} |
    1  | {} {} {} |
    0  | {} {} {} |
        ‾ ‾ ‾ ‾ 
         0 1 2
    """ 
    .format(
        v7,v8,v9,
        v4,v5,v6,
        v1,v2,v3
        )
    )

def check_if_game_over():

    def check_rows():
        row_0 = board[1][0] == board[1][0] == board[2][0] != " "
        row_1 = board[0][1] == board[1][1] == board[2][1] != " "
        row_2 = board[0][2] == board[1][2] == board[2][2] != " "
        return (row_0 or row_1 or row_2)

    def check_horizontals():
        horizontal_0 = board[0][0] == board[0][1] == board[0][2] != " "
        horizontal_1 = board[1][0] == board[1][1] == board[1][2] != " "
        horizontal_2 = board[2][0] == board[2][1] == board[2][2] != " "
        return (horizontal_0 or horizontal_1 or horizontal_2)

    def check_diagonals():
        diagonal_0 = board[0][0] == board[1][1] == board[2][2] != " "
        diagonal_1 = board[0][2] == board[1][1] == board[2][0] != " "
        return(diagonal_0 or diagonal_1)

    return check_rows() or check_horizontals() or check_diagonals()


def winner(winner):
    print("Congrats {}".format(winner))
    
def play_game(GameOver):

    print("X goes first")
    display_board(board[0][0],board[1][0],board[2][0],board[0][1],board[1][1],board[2][1],board[0][2],board[1][2],board[2][2])

    while (not GameOver):
        try:
            userInput = input("Coordinates For next Move: ")
            coordinates =  [int(x) for x in re.split('[^0-9]+',userInput)]
            if ((len(coordinates) != 2) or (coordinates[0] >= 3) or (coordinates[1] >= 3) or (coordinates[0] < 0) or (coordinates[1] < 0)):
                raise TypeError
            else:
                if board[coordinates[0]][coordinates[1]] == " ":  # check if empty
                    currentplayer = next(players) #Uses current play symbol then flips
                    board[coordinates[0]][coordinates[1]] = currentplayer
                    GameOver = check_if_game_over()
                else:
                    raise TypeError
                
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Invald Move")
            continue
        display_board(board[0][0],board[1][0],board[2][0],board[0][1],board[1][1],board[2][1],board[0][2],board[1][2],board[2][2])
    winner(currentplayer)

play_game(GameOver)


