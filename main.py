from tkinter import *
from PIL import Image, ImageTk
import random

background_color = "#D4ADFC"
second_color = "#5C469C"
label_color = "#0C134F"
custom_font = ("Lucida Handwriting", 20, "bold")
computer_score_value = 0
person_score_value = 0
win_score = 10
photo_list = []


def rock_paper_scissors(option):

    global computer_score_value
    global person_score_value
    computer_option = random.randint(0, 2)

    computer_canvas.delete("all")
    person_canvas.delete("all")

    computer_image = Image.open(f"./images/{computer_option}.png")
    computer_image = computer_image.resize((200, 200))
    computer_photo = ImageTk.PhotoImage(computer_image)
    photo_list.append(computer_photo)
    computer_canvas.create_image(150, 100, image=computer_photo)

    person_image = Image.open(f"./images/{option}.png")
    person_image = person_image.resize((200, 200))
    person_photo = ImageTk.PhotoImage(person_image)
    photo_list.append(person_photo)
    person_canvas.create_image(150, 100, image=person_photo)

    if option == computer_option:
        computer_score_value += 1
        person_score_value += 1
        computer_score.config(text=f"Score: {computer_score_value}", font=custom_font,
                              bg=background_color, fg=label_color)
        person_score.config(text=f"Score: {person_score_value}", font=custom_font,
                            bg=background_color, fg=label_color)
    elif option == 0 and computer_option == 1 or option == 1 and computer_option == 2 or \
            option == 2 and computer_option == 0:
        computer_score_value += 1
        computer_score.config(text=f"Score: {computer_score_value}", font=custom_font,
                              bg=background_color, fg=label_color)
    else:
        person_score_value += 1
        person_score.config(text=f"Score: {person_score_value}", font=custom_font,
                            bg=background_color, fg=label_color)

    if computer_score_value == win_score or person_score_value == win_score:
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissor_button.config(state="disabled")
        if computer_score_value == win_score and person_score_value == win_score:
            winner_label = Label(text="Tie!!!", font=custom_font, bg=background_color, fg=label_color)
        elif person_score_value == win_score:
            winner_label = Label(text="You Won!", font=custom_font, bg=background_color, fg=label_color)
        else:
            winner_label = Label(text="Computer Won!", font=custom_font, bg=background_color, fg=label_color)
        winner_label.grid(row=4, columnspan=3, column=0)


window = Tk()
window.title("Rock Paper Scissors")
window.minsize(width=800, height=600)
window.configure(bg=background_color, padx=70, pady=30)

computer_label = Label(text="Computer", font=custom_font, bg=background_color, fg=label_color)
computer_label.grid(row=0, column=0)

person_label = Label(text="You", font=custom_font, bg=background_color, fg=label_color)
person_label.grid(row=0, column=2)

computer_canvas = Canvas(width=300, height=200, bg=second_color)
computer_canvas.grid(row=1, column=0)

vs_label = Label(text="VS", font=custom_font, bg=background_color, fg=label_color)
vs_label.grid(row=1, column=1)

person_canvas = Canvas(width=300, height=200, bg=second_color)
person_canvas.grid(row=1, column=2, pady=30)

computer_score = Label(text=f"Score: {computer_score_value}", font=custom_font, bg=background_color, fg=label_color)
computer_score.grid(row=2, column=0)

person_score = Label(text=f"Score: {person_score_value}", font=custom_font, bg=background_color, fg=label_color)
person_score.grid(row=2, column=2)

image1 = Image.open("./images/0.png")
image1 = image1.resize((50, 50))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("./images/1.png")
image2 = image2.resize((50, 50))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("./images/2.png")
image3 = image3.resize((50, 50))
photo3 = ImageTk.PhotoImage(image3)

rock_button = Button(image=photo1, command=lambda: rock_paper_scissors(0))
rock_button.grid(row=3, column=0, pady=30)

paper_button = Button(image=photo2, command=lambda: rock_paper_scissors(1))
paper_button.grid(row=3, column=1, pady=30)

scissor_button = Button(image=photo3, command=lambda: rock_paper_scissors(2))
scissor_button.grid(row=3, column=2, pady=30)
window.mainloop()
