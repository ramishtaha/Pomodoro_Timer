from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global checkmarks
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text='00:00')
    checkmarks = ''
    checkmark_label.config(text=checkmarks)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global checkmarks

    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    time = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += '✔'
            checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Start Reset Buttons
start_btn = Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', command=reset_timer)
reset_btn.grid(column=2, row=2)

# Checkmark
checkmark_label = Label(text=checkmarks, fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)



window.mainloop()
