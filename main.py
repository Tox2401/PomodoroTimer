import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 1200
CYCLE = 0
TIMER = None


def countdown(count):
    global TIMER

    countMinutes = math.floor(count / 60)
    if countMinutes < 10:
        countMinutes = f"0{math.floor(count / 60)}"

    countSeconds = count % 60
    if countSeconds < 10:
        countSeconds = f"0{count % 60}"

    canvas.itemconfig(timerText, text=f"{countMinutes}:{countSeconds}")

    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        startCountdown()
        marks = ""
        for i in range(math.floor(CYCLE/2)):
            marks += "✔"
        checkMarks.config(text=marks)


def startCountdown():
    global CYCLE
    CYCLE += 1

    if CYCLE % 8 == 0:
        countdown(LONG_BREAK_MIN)
        timerLabel.config(text="Break", fg=RED)
    elif CYCLE % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        timerLabel.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN)
        timerLabel.config(text="Work", fg=GREEN)


def resetSession():
    global CYCLE
    global TIMER
    try:
        window.after_cancel(TIMER)
        CYCLE = 0
        canvas.itemconfig(timerText, text="25:00")
        checkMarks.config(text="")
        timerLabel.config(text="Pomodoro")
    except ValueError:
        print("Unable to reset, already at initial state.")
        pass


# ------------------------------------------- UI SETUP -------------------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

timerLabel = Label(text="Pomodoro", bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))
timerLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 135, text="25:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

startButton = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=startCountdown)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=resetSession)
resetButton.grid(column=2, row=2)

checkMarks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
checkMarks.grid(column=1, row=3)


window.mainloop()
