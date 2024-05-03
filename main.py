from tkinter import *
import pandas as p
import random as r


# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
Font_name = "Ariel"
current_card={}
to_learn = {}

# ---------------------------- CREATING FLASHCARD ------------------------------- #
try:
    data = p.read_csv("data_path")
except:
    original_data = p.read_csv("")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global current_card,delay
    window.after_cancel(delay)
    current_card = r.choice(to_learn)
    canvas.itemconfig(canvas_image,image=front_img)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    delay = window.after(3000,flip_card)

# ---------------------------- FLIP THE CARD ------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(title,text = "English",fill="white")
    canvas.itemconfig(word,text = current_card["English"],fill="white")

# ---------------------------- KNOWN FLASHCARD ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = p.DataFrame(to_learn)
    data.to_csv("data_path",index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

delay = window.after(3000,flip_card)

#CANVAS
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_img = PhotoImage(file="")
back_img = PhotoImage(file="")
canvas_image = canvas.create_image(400,263,image=front_img)
title = canvas.create_text(400,150,text="",font=(Font_name,40,"italic"))
word = canvas.create_text(400,263,text="",font=(Font_name,60,"bold"))
canvas.grid(column=0,row=0)

#BUTTONS
wrong_img = PhotoImage(file="")
wrong = Button(image=wrong_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
wrong.grid(column=0,row=1)


right_img = PhotoImage(file="")
right = Button(image=right_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right.grid(column=1,row=1)

next_card()


window.mainloop()
