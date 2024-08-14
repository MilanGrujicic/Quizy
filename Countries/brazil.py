from tkinter import messagebox
import turtle
import pandas

data = pandas.read_csv("Data/brazilian_states.csv")
states = data["state"].to_list()

screen = turtle.Screen()
screen.title("Brazil States Game")
screen.bgcolor("#39dbff")
image = "Maps/brazil_blank_states.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = set()
missing_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/27 Completed", prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        break

    if answer_state in states:
        guessed_states.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

if len(guessed_states) == 27:
    messagebox.showinfo(title="You Won!", message=f"Congratulations, you guessed all 27 states correctly.")
else:
    df = pandas.DataFrame(missing_states)
    df.to_csv("answers.csv")