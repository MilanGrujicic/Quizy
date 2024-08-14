import turtle
from tkinter import messagebox

import pandas

data = pandas.read_csv("Data/slovenian_regions.csv")
regions = data["regions"].to_list()

screen = turtle.Screen()
screen.setup(width=550, height=350)
screen.title("Slovenian Regions Game")
image = "Maps/slovenia_blank_regions.gif"
screen.addshape(image)
turtle.shape(image)
guessed_regions = set()
missing_regions = []

while len(guessed_regions) < 12:
    answer_region = screen.textinput(
        title=f"{len(guessed_regions)}/12 Regions Correct", prompt="What's another region?"
    ).title()

    if answer_region == "Exit":
        for region in regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        break

    if answer_region in regions:
        guessed_regions.add(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.regions == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)

if len(guessed_regions) == 12:
    messagebox.showinfo(title="You Won!", message=f"Congratulations, you guessed all 12 regions correctly.")
else:
    df = pandas.DataFrame(missing_regions)
    df.to_csv("answers.csv")

"""
Get x y coordinates on click

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
