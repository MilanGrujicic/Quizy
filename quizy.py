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
        logo = PhotoImage(file="quizyneo.png")
        canvas.create_image(200, 120, image=logo)

        # BUTTONS
        b_start = Button(text='Start Game', width=10, bg="#fff500", highlightbackground = "black", border="2", command=utils.start_game)
        b_start.grid(row=1, column=0, padx= 125, pady=5)
        b_options = Button(text='Options', width=10, bg="#fff500", highlightbackground = "black", border="2", command=utils.open_options)
        b_options.grid(row=2, column=0, pady=5)
        b_exit = Button(text='Exit', width=10, bg="#fff500", highlightbackground = "black", border="2", command=self.window.destroy)
        b_exit.grid(row=3, column=0, pady=5)

        # LABEL
        l_creator = Label(text='Made with love by Milan.', font=("Arial", 10, "italic"), fg='black', bg="#39dbff")
        l_creator.grid(row=4, column=0, sticky="SW", pady=40)

        self.window.mainloop()
