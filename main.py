from tkinter import *
import subprocess
# from playsound import playsound

def open_options():
    options = Toplevel(root)
    options.title("Quizy - Options")
    options.config(bg="#27262e")
    options.geometry("360x225")
    # playsound("button_sound.mp3")

def start_game():
    new_window = Toplevel(root)
    new_window.title("Pick a country")
    new_window.config(bg="#27262e")
    new_window.geometry("360x450")
    brazil_flag = PhotoImage(file="bra_flag.png")
    slovenia_flag = PhotoImage(file="Slovenia/slo_flag.png")
    china_flag = PhotoImage(file="China/chinese_flag.png")
    b_level_1 = Button(new_window, text="Brazil", image=brazil_flag, compound="top", padx=14, command=start_brazil_map)
    b_level_1.grid(row=0, column=0, padx=125, pady=5)
    b_level_2 = Button(new_window, text="Slovenia", image=slovenia_flag, compound="top")
    b_level_2.grid(row=1, column=0, padx=125, pady=5)
    b_level_3 = Button(new_window, text="China", image=china_flag, compound="top", padx=14)
    b_level_3.grid(row=2, column=0, padx=125, pady=5)
    new_window.mainloop()

def start_brazil_map():
    file_to_run = "brazil.py"
    subprocess.run(["python3", file_to_run])

# MAIN WINDOWN SETUP
root = Tk()
root.title("Quizy")
root.config(bg="#27262e")
root.geometry("360x450")

# LOGO
canvas = Canvas(root, bg="#27262e", highlightthickness=0)
canvas.grid(row=0, column=0)
logo = PhotoImage(file="quizy.png")
canvas.create_image(200, 120, image=logo)

# BUTTONS
b_start = Button(text='Start Game', width=10, command=start_game)
b_start.grid(row=1, column=0, padx= 125, pady=5)
b_options = Button(text='Options', width=10, command=open_options)
b_options.grid(row=2, column=0, pady=5)
b_exit = Button(text='Exit', width=10, command=root.destroy)
b_exit.grid(row=3, column=0, pady=5)

# LABEL
l_creator = Label(text='Made with love by Milan.', font=("Arial", 10, "italic"), fg='white', bg="#27262e")
l_creator.grid(row=4, column=0, sticky="SW", pady=45)

root.mainloop()
