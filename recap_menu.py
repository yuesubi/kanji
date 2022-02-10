# -*- encode: utf-8 -*-

import time
from tkinter import *

from menu import Menu
from data import Data, Kanji

import res.assets as assets
import res.font as font
import res.shm as shm


class RecapMenu(Menu):
    def __init__(self, tk, manager):
        super(Menu, self).__init__()

        self.frame = Frame(tk, bg=shm.bg)

        self.title_l = Label(self.frame, text="Recap", font=font.en(20), fg=shm.fg, bg=shm.bg)
        self.title_l.place(x=20, y=20)

        self.leave_b = Button(self.frame, text="leave", font=font.en(12), fg=shm.fg, bg=shm.bg, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.leave_b.place(x=20, y=405)
