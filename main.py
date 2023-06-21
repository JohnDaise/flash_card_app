from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Arial", 40, "italic")
CARD_FONT = ("Arial", 60, "bold")


# IMPORT FLASH CARD DATA
data = pandas.read_csv("data/french_words.csv")
words_to_learn = data.to_dict(orient="records")  # orient records converts to a list with french
# print(words_to_learn)


def next_card():
    current_word = random.choice(words_to_learn)
    print(current_word['French'])
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_text, text=current_word['French'])


# UI

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# IMAGES
card_image = PhotoImage(file='./images/card_front.png')
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

# CARD
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 150, text="", font=CARD_TITLE_FONT)
card_text = canvas.create_text(400, 263, text="", font=CARD_FONT)
canvas.itemconfig(card_title, fill='black')
canvas.itemconfig(card_text, fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
known_button = Button(image=right_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
