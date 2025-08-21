
from tkinter import *
import random
def next_turn(row,column):
    global players
    if Buttons[row][column]["text"]=="" and check_winner() is False:
        if players==player[0]:
            Buttons[row][column]["text"]=players
            if check_winner() is False:
                players=player[1]
                label.config(text=player[1]+"'S Turn")
            elif check_winner() is True:
                 label.config(text=player[0] + "wins")
            elif check_winner() == "Tie":
                return "Tie"
        else:
            Buttons[row][column]["text"] = players
            if check_winner() is False:
                players = player[0]
                label.config(text=player[0] + "'S Turn")
            elif check_winner() is True:
                label.config(text=player[1] + "wins")
            elif check_winner() == "Tie":
                return "Tie"
def check_winner():
    for row in range(3):
        if Buttons[row][0]["text"] == Buttons[row][1]["text"] == Buttons[row][2]["text"] != "":
           Buttons[row][0].config(bg="green")
           Buttons[row][1].config(bg="green")
           Buttons[row][2].config(bg="green")
           return True
    for column in range(3):
        if Buttons[0][column]["text"] == Buttons[1][column]["text"] == Buttons[2][column]["text"] != "":
           Buttons[0][column].config(bg="green")
           Buttons[1][column].config(bg="green")
           Buttons[2][column].config(bg="green")
           return True
    if Buttons[0][0]["text"] == Buttons[1][1]["text"] == Buttons[2][2]["text"] != "":
        Buttons[0][0].config(bg="green")
        Buttons[1][1].config(bg="green")
        Buttons[2][2].config(bg="green")
        return True
    elif Buttons[0][2]["text"] == Buttons[1][1]["text"] == Buttons[2][0]["text"] != "":
        Buttons[0][2].config(bg="green")
        Buttons[1][1].config(bg="green")
        Buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                    Buttons[row][column].config(bg="yellow")

        return "Tie"
    else:
        return False

def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if Buttons[row][column]["text"]!="":
                spaces -=1
    if spaces==0:
        return False
    else:
        return True



player=["x","o"]
players=random.choice(player)

window=Tk()

label=Label(window,text=players + "'S Turn",font=("Ariel",20))
label.pack()

frame=Frame(window)
frame.pack()

Buttons=[["0","0","0"],
         ["0","0","0"],
         ["0","0","0"]]

for row in range(3):
    for column in range(3):
        Buttons[row][column]=Button(frame,width=5,height=3,command= lambda rows=row,columns=column :next_turn(rows,columns) )
        Buttons[row][column].grid(row=row,column=column)

window.mainloop()

