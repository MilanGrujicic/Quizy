from tkinter import *
from tkinter import messagebox
import subprocess
import quizy

def open_options():
    '''From initial screen, opens Options dialog.'''
    options_dialog = Toplevel()
    options_dialog.title("Quizy - Options")
    options_dialog.config(bg="#39dbff")
    options_dialog.geometry("360x225")

def start_game():
    '''From initial screen, opens start game screen.'''
    start_game_screen = quizy.start_game()

def start_chosen_map(country, division):
    '''From start game screen, opens the country map picked by the user.'''
    if country == "china":
        chinese_map = quizy.chinese_map()
    open_instructions(country, division)
    file_to_run = f"{country}.py"
    subprocess.run(["python3", file_to_run])

def open_instructions(contry, division):
    '''Displays dialog with instructions.'''
    messagebox.showinfo(title="Instructions", message=f"You will be prompted with the map of {contry.title()}.\nTry to guess all its {division}.\nHave fun.")
