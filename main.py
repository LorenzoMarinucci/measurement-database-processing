import tkinter as tk

from gui.gui import GUI

def main() -> None:
    window = tk.Tk()
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
