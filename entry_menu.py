# -*- encode: utf-8 -*-

from tkinter import *

from menu import Menu

import res.font as font
import res.shm as shm


class EntryMenu(Menu):
    def __init__(self, tk):
        super(Menu, self).__init__()

        self.frame = Frame(tk, bg=shm.bg)

        self.fg_l = Label(self.frame, text="日 月", font=font.jp(200), fg=shm.red, bg=shm.bg)
        self.fg_l.place(x=0, y=0)

        self.start_b = Button(self.frame, text="START", font=font.en(46), fg=shm.fg, bg=shm.curr, relief='flat')
        self.start_b.place(x=60, y=100)
