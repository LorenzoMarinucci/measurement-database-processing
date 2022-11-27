import os
import sys
import tkinter as tk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry

from params.params import ConsoleParams
#from processing.dataframeprocessing import process_dataset

def main() -> None:
    window = tk.Tk()
    gui = GUI(window)
    window.mainloop()

    filename = _get_filename()
    day_start, day_end = _get_day_start_and_end()
    hour_start, hour_end = _get_hour_start_and_end()
    sdv = _get_standard_deviation()

    #process_dataset(filename, hour_start, hour_end, day_start, day_end, sdv)


def _get_filename() -> str:
    try:
        filename_index = sys.argv.index(ConsoleParams.FILENAME.value)
        return sys.argv[filename_index + 1]
    except ValueError:
        raise Exception("Filename param is mandatory.") from None


def _get_day_start_and_end() -> tuple[str | None, str | None]:
    try:
        day_start_index = sys.argv.index(ConsoleParams.DAY_START.value)
        day_start = sys.argv[day_start_index + 1]
    except ValueError:
        day_start = None

    try:
        day_end_index = sys.argv.index(ConsoleParams.DAY_END.value)
        day_end = sys.argv[day_end_index + 1]
    except ValueError:
        day_end = None

    return day_start, day_end


def _get_hour_start_and_end() -> tuple[str | None, str | None]:
    try:
        hour_start_index = sys.argv.index(ConsoleParams.HOUR_START.value)
        hour_start = sys.argv[hour_start_index + 1]
    except ValueError:
        hour_start = None

    try:
        hour_end_index = sys.argv.index(ConsoleParams.HOUR_END.value)
        hour_end = sys.argv[hour_end_index + 1]
    except ValueError:
        hour_end = None

    return hour_start, hour_end


def _get_standard_deviation() -> int | None:
    try:
        sdv_index = sys.argv.index(ConsoleParams.STANDARD_DEVIATION.value)
        sdv = int(sys.argv[sdv_index + 1])
    except ValueError:
        sdv = None

    return sdv

class GUI(object):
    file = ""

    def __init__(self, window):
        self.window = window
        window.geometry("300x300+10+10")
        window.resizable(width=False, height=False)
        window.title('Measurement Database Processing')

        def value(selection):
            self.file = selection

        # Create files dropdown
        options = os.listdir("./datasets")
        clicked = tk.StringVar()
        clicked.set("Select dataset")
        drop = tk.OptionMenu(window, clicked, *options, command=value)
        drop.pack()

        # Processing label options
        lbl = tk.Label(window, text="Select processing options", fg='black', font=("Helvetica", 10))
        lbl.place(x=70, y=50)

        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()
        v4 = tk.IntVar()
        v5 = tk.IntVar()

        entry1 = tk.Entry(width=8)
        entry1.place(x=150, y=100)
        entry2 = tk.Entry(width=8)
        entry2.place(x=150, y=130)
        entry3 = tk.Entry(width=8)
        entry3.place(x=150, y=160)
        entry4 = tk.Entry(width=8)
        entry4.place(x=150, y=190)
        entry5 = tk.Entry(width=8)
        entry5.place(x=150, y=220)

        def activateCheck1():
            if v1.get() == 1:  # whenever checked
               entry1.config(state="normal")
            elif v1.get() == 0:  # whenever unchecked
               entry1.config(state="disabled")

        def activateCheck2():
            if v2.get() == 1:  # whenever checked
               entry2.config(state="normal")
            elif v2.get() == 0:  # whenever unchecked
               entry2.config(state="disabled")

        def activateCheck3():
            if v3.get() == 1:  # whenever checked
               entry3.config(state="normal")
            elif v3.get() == 0:  # whenever unchecked
               entry3.config(state="disabled")

        def activateCheck4():
            if v4.get() == 1:  # whenever checked
               entry4.config(state="normal")
            elif v4.get() == 0:  # whenever unchecked
               entry4.config(state="disabled")

        def activateCheck5():
            if v5.get() == 1:  # whenever checked
               entry5.config(state="normal")
            elif v5.get() == 0:  # whenever unchecked
               entry5.config(state="disabled")

        C1 = tk.Checkbutton(window, text="Start date", variable=v1, command=activateCheck1)
        C2 = tk.Checkbutton(window, text="End date", variable=v2, command=activateCheck2)
        C3 = tk.Checkbutton(window, text="Start hour", variable=v3, command=activateCheck3)
        C4 = tk.Checkbutton(window, text="End hour", variable=v4, command=activateCheck4)
        C5 = tk.Checkbutton(window, text="Std. Dev.", variable=v5, command=activateCheck5)
        C1.place(x=50, y=100)
        C2.place(x=50, y=130)
        C3.place(x=50, y=160)
        C4.place(x=50, y=190)
        C5.place(x=50, y=220)

        entry1.config(state="disabled")
        entry2.config(state="disabled")
        entry3.config(state="disabled")
        entry4.config(state="disabled")
        entry5.config(state="disabled")

        def process():
            if self.file != "":
                return
                #if
            else:
                print("Debe elegir un archivo")

        submit = tk.Button(text="Submit", command=process)
        submit.place(x=120, y=260)


if __name__ == '__main__':
    main()
