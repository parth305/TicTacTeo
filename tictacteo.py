from tkinter import *
import random


def new_game():
    global player
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
    player = random.choice(players)
    label.config(text=player + " turn")


def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                return True

    return False


def cheack_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False


def next_trun(row, column):
    global player

    if buttons[row][column]["text"] == "" and cheack_winner() is False:

        if player == players[0]:
            buttons[row][column]["text"] = player
            if cheack_winner() is True:
                label.config(text=player + " wins")
            elif cheack_winner() is False:
                player = players[1]
                label.config(text=player + " turn")
            elif cheack_winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]["text"] = player

            if cheack_winner() is True:
                label.config(text=player + " wins")
            elif cheack_winner() is False:
                player = players[0]
                label.config(text=player + " turn")
            elif cheack_winner() == "Tie":
                label.config(text="Tie")


window = Tk()
window.title("Tic Tac Toe")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=("consolas", 40))
label.pack()

reset_button = Button(text="reset", font=("consolas", 20), command=new_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", command=lambda row=row, column=column:
        next_trun(row, column), font=("consolas", 40), width=5, height=2)
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)

window.mainloop()
