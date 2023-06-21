from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Arial", 40, "italic")
CARD_FONT = ("Arial", 60, "bold")

# UI

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_image = PhotoImage(file='./images/card_front.png')
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

#Card
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 150, text="Title", font=CARD_TITLE_FONT)
card_text = canvas.create_text(400, 263, text="Word", font=CARD_FONT)
canvas.itemconfig(card_title, fill='black')
canvas.itemconfig(card_text, fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
known_button = Button(image=right_image, highlightthickness=0)
known_button.grid(column=1, row=1)

unknown_button = Button(image=wrong_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

window.mainloop()
