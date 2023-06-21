from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



# UI

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_image = PhotoImage(file='./images/card_front.png')
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

#Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_image)
canvas.grid(column=0, row=0)

# Buttons
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=2, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
