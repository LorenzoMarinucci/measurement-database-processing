import os
import sys
import tkinter as tk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import re

from params.params import ConsoleParams
from processing.dataframeprocessing import process_dataset

def main() -> None:
    window = tk.Tk()
    gui = GUI(window)
    window.mainloop()

class GUI(object):
    file = ""

    def __init__(self, window):
        self.window = window
        window.geometry("300x500+10+10")
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
        entry5.insert(0, 3)

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

        errors = tk.Text(window, height=10, width=32, fg='red', wrap='word')
        errors.pack()
        errors.place(x=20, y= 300)

        def process():
            errorMessage = ""
            start_date = entry1.get()
            end_date = entry2.get()
            start_hour = entry3.get()
            end_hour = entry4.get()
            std = entry5.get()
            datePattern = re.compile("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$")
            timePattern = re.compile("^(((([0-1][0-9])|(2[0-3])):?[0-5][0-9]:?[0-5][0-9]+$))")
            if self.file == "":
                errorMessage += "* Debe elegir un archivo\n"
            if v1.get() == 1 and (start_date == "" or not datePattern.match(start_date)):
                errorMessage += "* Debe ingresar una fecha de inicio válida\n"
            if v2.get() == 1 and (end_date == "" or not datePattern.match(end_date)):
                errorMessage += "* Debe ingresar una fecha de fin válida\n"
            if v3.get() == 1 and (start_hour == "" or not timePattern.match(start_hour)):
                errorMessage += "* Debe ingresar una hora de inicio válida\n"
            if v4.get() == 1 and (end_hour == "" or not timePattern.match(end_hour)):
                errorMessage += "* Debe ingresar una hora de fin válida\n"
            if v5.get() == 1 and std == "":
                errorMessage += "* Debe ingresar un valor de desviación estandar válido"
            if errorMessage == "":
                start_date = None if start_date == "" else start_date
                end_date = None if end_date == "" else end_date
                start_hour = None if start_hour == "" else start_hour
                end_hour = None if end_hour == "" else end_hour
                if std == "":
                    std = 3
                process_dataset(self.file, start_hour, end_hour, start_date, end_date, int(std))
            else:
                errors.delete('1.0', tk.END)
                errors.insert(tk.END, errorMessage)

        submit = tk.Button(text="Submit", command=process)
        submit.place(x=120, y=260)


if __name__ == '__main__':
    main()
