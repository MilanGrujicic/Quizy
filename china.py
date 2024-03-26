import turtle
import pandas

data = pandas.read_csv("Data/chinese_provinces.csv")
provinces = data["provinces"].to_list()

screen = turtle.Screen()
screen.title("China Province Game")
screen.bgcolor("#39dbff")
image = "Maps/china_blank_provinces.gif"
screen.addshape(image)
turtle.shape(image)
guessed_provinces = set()
missing_provinces = list()

# def get_mouse_click_coor(x, y):
#     print(x, y)

while len(guessed_provinces) < 28:
    answer_province = screen.textinput(
        f"{len(guessed_provinces)}/28 completed", prompt="What's another province's name?"
    ).title()

    if answer_province == "Exit":
        for province in provinces:
            if province not in guessed_provinces:
                missing_provinces.append(province)
        break

    if answer_province in provinces:
        guessed_provinces.add(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.provinces == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province)
    
    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()

df = pandas.DataFrame(missing_provinces)
df.to_csv("answer.csv")