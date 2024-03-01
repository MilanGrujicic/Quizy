from tkinter import *

# MAIN WINDOWN SETUP
root = Tk()
root.title("Quizy")
root.config(bg="#27262e")
root.geometry("350x450")

# BUTTONSs
b_start = Button(text='Start Game', width=10)
b_start.grid(row=0, column=0, padx= 125, pady=5)
b_options = Button(text='Option', width=10)
b_options.grid(row=1, column=0, pady=5)
b_exit = Button(text='Exit', width=10)
b_exit.grid(row=2, column=0, pady=5)

root.mainloop()