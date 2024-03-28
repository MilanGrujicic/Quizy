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

def open_chinese_map():
    chinese_map = Toplevel()
    chinese_map.title("Pick an option")
    chinese_map.config(bg="#39dbff")
    chinese_map.geometry("450x150")

    pick_an_option = Label(chinese_map, text="Pick which map you want to play", font=("Arial", 15, "bold"), fg='black', bg="#39dbff")
    pick_an_option.grid(row=0, column=0, padx=25, pady=25)

    button_frame = Frame(chinese_map, bg="#39dbff")
    button_frame.grid(row=1,column=0)

    chinese_map_by_china = Button(button_frame, text="Chinese Map By China", bg="#fff500", highlightbackground = "black", bd=100, border="2", command=lambda: start_chosen_map("china", "provinces"))
    chinese_map_by_china.pack(side=LEFT, padx=5)

    chinese_map_by_western_countries = Button(button_frame, text="Chinese Map By Western Countries", bg="#fff500", highlightbackground = "black", bd=100, border="2", command=lambda: start_chosen_map("china_by_western_countries", "provinces"))
    chinese_map_by_western_countries.pack(side=RIGHT, padx=5)

def start_chosen_map(country, division):
    '''From start game screen, opens the country map picked by the user.'''
    open_instructions(country, division)
    file_to_run = f"{country}.py"
    subprocess.run(["python3", file_to_run])

def open_instructions(contry, division):
    '''Displays dialog with instructions.'''
    messagebox.showinfo(title="Instructions", message=f"You will be prompted with the map of {contry.title()}.\nTry to guess all its {division}.\nHave fun.")
