from tkinter import *
import math
import winsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PINK_RED="#FF4162"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=PINK_RED)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        winsound.Beep(440, 500)
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark +="🐈"
        check_marks.config(text=mark)





window=Tk()
window.title("Cat pomorodo")
window.config(padx=100,pady=60,bg=YELLOW)

title_label=Label(text="Timer",fg=PINK_RED,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1, row=0)

canvas=Canvas(width=298,height=195,bg=YELLOW,highlightthickness=0,highlightcolor=YELLOW)
cat_jpeg=PhotoImage(file="images-removebg-preview.png")
canvas.create_image(142,97,image=cat_jpeg)
timer_text=canvas.create_text(142,110,text="00:00",fill="pink",font=("Corier",35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start Cat Time",highlightthickness=0,fg=PINK_RED,command=start_timer)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset The Cat",highlightthickness=0,fg=PINK_RED,command=reset_timer)
reset_button.grid(column=3,row=2)

check_marks=Label(text="",fg=PINK_RED,bg=YELLOW,font=50)
check_marks.grid(column=1,row=2)

window.mainloop()