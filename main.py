from tkinter import *
import random
from para import the_para

TYPING_SEC = 60


def start_timer():
    input_field.delete(0, END)

    with open('highest_record', 'r') as file:
        highest_ = file.read()
    highest_speed = Label(text=f'Highest Speed: {highest_}')
    highest_speed.grid(row=1, column=1)

    count_sec = TYPING_SEC
    type_test_time(count_sec)
    text = random.choice(the_para)
    canvas.itemconfig(para_text, text=text, font=('Arial', 12))


def type_test_time(count_sec):
    if int(count_sec) < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=count_sec)
    if int(count_sec) > 0:
        window.after(1000, type_test_time, int(count_sec) - 1)
    else:
        wpm_label.config(text=f'WPM: {len(input_field.get().split())}', font=('Arial', 12, 'bold'))
        with open('highest_record', 'w') as file:
            file.write(f'{len(input_field.get().split())}')


window = Tk()
window.title("Type Test")
window.minsize(height=400, width=600)

canvas = Canvas(height=250, width=600)
timer_text = canvas.create_text(300, 35, text="00", font=("Arial", 20, "bold"))
para_text = canvas.create_text(300, 130, width=500, text="")
canvas.grid(row=2, column=1)

input_field = Entry()
input_field.grid(row=3, column=1)

wpm_label = Label(text="WPM: --", font=('Arial', 12, 'bold'), pady=7)
wpm_label.grid(row=4, column=1)

start_type_speed = Button(text="Start TypeTest", command=start_timer)
start_type_speed.grid(row=5, column=1)

window.mainloop()
