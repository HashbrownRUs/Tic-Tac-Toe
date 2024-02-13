# Board.py
import sys, re
from itertools import cycle
import PySimpleGUI as sg
from Again import again

GameOver = False
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
players = cycle(["X","O"]) 

Blank = "Assets\White_Square_100x100.png"
Cross = "Assets\Cross1_100x100.png"
Circle = "Assets\Circle_100x100.png"

sg.theme_background_color(color = "white") 

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
    return ("Congrats {}".format(winner))

def Game(GameOver):

    lastEvent = " "
    
    layout = [
        [
        sg.Button(image_filename=Blank, key='0 2',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='1 2',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='2 2',  button_color=sg.theme_background_color(), border_width=0)
        ],
        [
        sg.Button(image_filename=Blank, key='0 1',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='1 1',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='2 1',  button_color=sg.theme_background_color(), border_width=0)
        ],
        [
        sg.Button(image_filename=Blank, key='0 0',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='1 0',  button_color=sg.theme_background_color(), border_width=0),sg.Button(image_filename=Blank, key='2 0',  button_color=sg.theme_background_color(), border_width=0)
        ]
    ], 

    # Create the window
    window = sg.Window("Tic Tac Toe", layout, background_color="black")

    # Create an event loop
    while True:
        event, value = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        if (not GameOver):
            try:
                if (event != lastEvent):
                    coordinates =  [int(x) for x in re.split('[^0-9]+',(event))]
                    if board[coordinates[0]][coordinates[1]] == " ":  # check if empty
                        currentplayer = next(players) #Uses current play symbol then flips
                        board[coordinates[0]][coordinates[1]] = currentplayer
                        if currentplayer == "X":
                            window[event].update(image_filename = Cross)
                        else:
                            window[event].update(image_filename = Circle)
                        GameOver = check_if_game_over()
                        if (GameOver):
                            sg.popup_timed(winner(currentplayer))
                            again()
                            window.close()
                    else:
                        raise TypeError
                else:
                    raise TypeError
                
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Invald Move")
                continue
            lastEvent = event

    window.close()

Game(GameOver)
