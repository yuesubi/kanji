# -*- encode: utf-8 -*-

from tkinter import *

from menu_manager import Manager

import res.font as font
import res.shm as shm


class App:
    def __init__(self):
        # WINDOW
        self.tk = Tk()
        self.tk.title("TODO")
        self.tk.resizable(False, False)
        self.tk.geometry("640x460")

        self.tk.config(bg=shm.bg)

        Manager.init(self.tk, "entry_menu")

    def run(self) -> None:
        self.tk.mainloop()
