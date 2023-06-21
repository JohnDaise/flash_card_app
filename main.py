from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Arial", 40, "italic")
CARD_FONT = ("Arial", 60, "bold")

current_card = {}
to_learn = {}


# IMPORT FLASH CARD DATA
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# IMAGES
card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

# CARD
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="", font=CARD_TITLE_FONT)
card_text = canvas.create_text(400, 263, text="", font=CARD_FONT)
canvas.itemconfig(card_title, fill='black')
canvas.itemconfig(card_text, fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
known_button = Button(image=right_image, highlightthickness=0, command=is_known_card)
known_button.grid(column=1, row=1)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card())
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
