import tkinter as tk

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    reps = 0
    start_button["state"] = "normal"
    title_label["text"] = "Timer"
    canvas.itemconfig(canvas_text, text="00:00")
    checkmarks.set("")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    start_button["state"] = "disabled"
    reset_button["state"] = "normal"
    if reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    else:
        title_label.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def sec_to_time(seconds):
    minutes = seconds // 60
    seconds -= minutes * 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"


def countdown(count):
    global timer
    global reps
    canvas.itemconfig(canvas_text, text=sec_to_time(count))
    if count > 0:
        timer = window.after(998, countdown, count - 1)
    else:
        start_timer()
        for _ in range(reps // 2):
            checkmarks.set(f"{checkmarks.get()} ✔")


# --------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)

title_label = tk.Label(window, text="Timer", font=(FONT_NAME, 50), background=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

tomato_photo = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 111, image=tomato_photo)
canvas_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = tk.Button(window, text="Start", bg="white", borderwidth=0, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(window, text="Reset", bg="white", state="disabled", borderwidth=0, highlightthickness=0,
                         command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = tk.StringVar(window)
checkmark_label = tk.Label(window, textvariable=checkmarks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkmark_label.grid(row=3, column=1)

window.mainloop()
