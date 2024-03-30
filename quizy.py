from tkinter import *
import utils

class Quizy:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizy")
        self.window.config(bg="#39dbff")
        self.window.geometry("360x450")

        # LOGO
        canvas = Canvas(self.window, bg="#39dbff", highlightthickness=0)
        canvas.grid(row=0, column=0)
        logo = PhotoImage(file="logo.png")
        canvas.create_image(200, 120, image=logo)

        # BUTTONS
        start_game = Button(text='Start Game', width=10, bg="#fff500", highlightbackground = "black", border="2", command=utils.start_game)
        start_game.grid(row=1, column=0, padx= 125, pady=5)
        exit = Button(text='Exit', width=10, bg="#fff500", highlightbackground = "black", border="2", command=self.window.destroy)
        exit.grid(row=2, column=0, pady=5)

        # LABEL
        l_creator = Label(text='Made with love by Milan.', font=("Arial", 10, "italic"), fg='black', bg="#39dbff")
        l_creator.grid(row=3, column=0, sticky="SW", pady=80)

        self.window.mainloop()

class start_game(Quizy):
    def __init__(self):
        self.start_game_window = Toplevel()
        self.start_game_window.title("Pick a country")
        self.start_game_window.config(bg="#39dbff")
        self.start_game_window.geometry("360x450")

        brazilian_flag = PhotoImage(file="Flags/bra_flag.png")
        slovenian_flag = PhotoImage(file="Flags/slo_flag.png")
        chinese_flag = PhotoImage(file="Flags/chinese_flag.png")

        self.label_pick_a_country = Label(self.start_game_window, text="Pick A Country", font=("Arial", 15, "bold"), fg='black', bg="#39dbff")
        self.label_pick_a_country.grid(row=0, column=0)

        self.brazilian_map = Button(self.start_game_window, text="Brazil", image=brazilian_flag, compound="top", padx=30, bg="#fff500", highlightbackground = "black", bd=100, border="2",command=lambda: utils.start_chosen_map("brazil", "states"))
        self.brazilian_map.grid(row=1, column=0, padx=125, pady=5)
        self.slovenian_map = Button(self.start_game_window, text="Slovenia", image=slovenian_flag, compound="top", padx=27, bg="#fff500", highlightbackground = "black", bd=100, border="2", command=lambda: utils.start_chosen_map("slovenia", "regions"))
        self.slovenian_map.grid(row=2, column=0, padx=125, pady=5)
        self.chinese_map = Button(self.start_game_window, text="China", image=chinese_flag, compound="top", padx=30, bg="#fff500", highlightbackground = "black", bd=100, border="2", command= utils.open_chinese_map)
        self.chinese_map.grid(row=3, column=0, padx=125, pady=5)
        self.button_exit = Button(self.start_game_window, text="Back", width=10, compound="left", padx=14, bg="#fff500", highlightbackground = "black", bd=100, border="2", command=self.start_game_window.destroy)
        self.button_exit.grid(row=4, column=0, padx=125, pady=25)

        self.start_game_window.mainloop()

