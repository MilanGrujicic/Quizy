from tkinter import *

# BUTTON FUNCTIONS
def open_options():
    options = Toplevel(root)
    options.title("Quizy - Options")
    options.config(bg="#27262e")
    options.geometry("360x225")

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
b_start = Button(text='Start Game', width=10)
b_start.grid(row=1, column=0, padx= 125, pady=5)
b_options = Button(text='Option', width=10, command=open_options)
b_options.grid(row=2, column=0, pady=5)
b_exit = Button(text='Exit', width=10, command=root.destroy)
b_exit.grid(row=3, column=0, pady=5)

# LABEL
l_creator = Label(text='Made with love by Milan.', font=("Arial", 10, "italic"), fg='white', bg="#27262e")
l_creator.grid(row=4, column=0, sticky="SW", pady=45)

root.mainloop()