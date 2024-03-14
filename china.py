import turtle
import pandas

data = pandas.read_csv("provinces.csv")
provinces = data["provinces"].to_list()

screen = turtle.Screen()
screen.title("China Province Game")
screen.bgcolor("#39dbff")
image = "blank_provinces_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_provinces = []

while len(guessed_provinces) < 20:
    answer_province = screen.textinput(
        f"{len(guessed_provinces)}/20 completed", prompt="What's another province's name?"
    ).title()

    if answer_province == "Exit":
        missing_states = []
        for province in provinces:
            if province not in guessed_provinces:
                missing_states.append(province)
        break

    if answer_province in provinces:
        guessed_provinces.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.provinces == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province)

df = pandas.DataFrame(missing_states)
df.to_csv("answer.csv")