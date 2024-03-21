from tkinter import *
import subprocess

def open_options():
    options_dialog = Toplevel()
    options_dialog.title("Quizy - Options")
    options_dialog.config(bg="#39dbff")
    options_dialog.geometry("360x225")

def start_game():
    start_game_window = Toplevel()
    start_game_window.title("Pick a country")
    start_game_window.config(bg="#39dbff")
    start_game_window.geometry("360x450")

    brazil_flag = PhotoImage(file="Flags/bra_flag.png")
    slovenia_flag = PhotoImage(file="Flags/slo_flag.png")
    china_flag = PhotoImage(file="Flags/chinese_flag.png")
    
    l_pick_country = Label(start_game_window, text="Pick A Country", font=("Arial", 15, "bold"), fg='black', bg="#39dbff")
    l_pick_country.grid(row=0, column=0)

    b_level_1 = Button(start_game_window, text="Brazil", image=brazil_flag, compound="top", padx=30, bg="#fff500", highlightbackground = "black", bd=100, border="2",command=lambda: start_chosen_map("brazil"))
    b_level_1.grid(row=1, column=0, padx=125, pady=5)
    b_level_2 = Button(start_game_window, text="Slovenia", image=slovenia_flag, compound="top", padx=27, bg="#fff500", highlightbackground = "black", bd=100, border="2", command=lambda: start_chosen_map("slovenia"))
    b_level_2.grid(row=2, column=0, padx=125, pady=5)
    b_level_3 = Button(start_game_window, text="China", image=china_flag, compound="top", padx=30, bg="#fff500", highlightbackground = "black", bd=100, border="2", command=lambda: start_chosen_map("china"))
    b_level_3.grid(row=3, column=0, padx=125, pady=5)
    b_exit = Button(start_game_window, text="Back", width=10, compound="left", padx=14, bg="#fff500", highlightbackground = "black", bd=100, border="2", command=start_game_window.destroy)
    b_exit.grid(row=4, column=0, padx=125, pady=25)
    
    start_game_window.mainloop()

def start_chosen_map(country):
    file_to_run = f"{country}.py"
    subprocess.run(["python3", file_to_run])