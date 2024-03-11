import turtle
import pandas

data = pandas.read_csv("regions.csv")
regions = data["regions"].to_list()

screen = turtle.Screen()
screen.setup(width=550, height=350)
screen.title("Slovenian Regions Game")
image = "blank_regions_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_regions = []

while len(guessed_regions) < 12:
    answer_region = screen.textinput(
        title=f"{len(guessed_regions)}/12 Regions Correct", prompt="What's another region?"
    ).title()

    if answer_region == "Exit":
        missing_regions = []
        for region in regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        break

    if answer_region in regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.regions == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)

df = pandas.DataFrame(missing_regions)
df.to_csv("answers.csv")

"""
Get x y coordinates on click

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
