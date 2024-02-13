import PySimpleGUI as sg

def again():
    if sg.popup_yes_no("Do you want to play again?") == 'Yes':
        from Game_Main import Game

