import turtle
import pandas

data = pandas.read_csv("states.csv")
states = data["state"].to_list()

screen = turtle.Screen()
screen.title("Brazil States Game")
screen.bgcolor("#27262e")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/27 Completed", prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

df = pandas.DataFrame(missing_states)
df.to_csv("answer.csv")
