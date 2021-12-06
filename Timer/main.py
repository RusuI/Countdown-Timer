import threading
import time
import tkinter as tk
from tkinter import messagebox, END, DISABLED
import playsound as playsound
from win10toast import ToastNotifier
from playsound import playsound


window = tk.Tk()
window.title('Countdown Timer')
window.iconbitmap('C:/Users/Ioana/PycharmProjects/Timer/venv/timer_icon.ico')
# Define image
my_img = tk.PhotoImage(file="C:/Users/Ioana/PycharmProjects/Timer/venv/timer.png")
# Create a label
my_label = tk.Label(window, image=my_img)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# setting the geometry of the window
window.geometry("600x500")

hour = tk.StringVar()
hour.set("00")

minute = tk.StringVar()
minute.set("00")

second = tk.StringVar()
second.set("00")

# Take the input from the user

hourEntry = tk.Entry(window, bg="green", bd=3, width=3, font=("Arial", 18, ""),
                     textvariable=hour)
hourEntry.place(x=120, y=20)

minuteEntry = tk.Entry(window, bg="blue", bd=3, width=3, font=("Arial", 18, ""),
                       textvariable=minute)
minuteEntry.place(x=170, y=20)

secondEntry = tk.Entry(window, bg="yellow", bd=3, width=3, font=("Arial", 18, ""),
                       textvariable=second)
secondEntry.place(x=220, y=20)

running = False
reset = False
stop = False


def submit_reset():
    print("buzz")
    global reset
    reset = True


pressed = True

def submit_stop():
    print("de cee")
    global stop
    stop = not stop
    global pressed
    if pressed:
        btn_stop.configure(bg="yellow")
    else:
        btn_stop.configure(bg="blue")
    pressed = not pressed


def thread_function():
    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    while temp > -1:

        global reset
        if reset:
            reset = False
            hourEntry.delete(0, END)
            minuteEntry.delete(0, END)
            secondEntry.delete(0, END)

            hour.set("00")
            minute.set("00")
            second.set("00")

            window.update()
            global running
            running = False
            break
        if stop:
            while stop:
                print("aicii")
                time.sleep(0.5)
        else:
            running = False

        print("continuarea")
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        window.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            # messagebox.showinfo("Time Countdown", "Time's up ")
            toast = ToastNotifier()
            toast.show_toast("Time Countdown", "Time is up", duration=10)
            playsound("C:/Users/Ioana/PycharmProjects/Timer/venv/beep.mp3")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


def submit():
    global running
    if not running:
        thread = threading.Thread(target=thread_function)
        thread.start()
        running = True


# button widget
btn_start = tk.Button(window, text='Start', bd='5', bg="blue",
                      command=submit
                      )
btn_start.place(x=120, y=120)
btn_reset = tk.Button(window, text='Reset', bd='5', bg="blue",
                      command=submit_reset
                      )
btn_reset.place(x=170, y=120)
btn_stop = tk.Button(window, text='Stop', bd='5', bg="blue",
                     command=submit_stop
                     )
btn_stop.place(x=223, y=120)

window.mainloop()
