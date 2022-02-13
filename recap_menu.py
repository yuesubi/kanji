# -*- encode: utf-8 -*-

import time
from tkinter import *

from menu import Menu
from data import Data, Kanji

import res.assets as assets
import res.font as font
import res.shm as shm


def readable_time(seconds):
    readable = str()

    if seconds < 60:
        readable = "in less than a minute"
    elif seconds < 3600:
        readable = f"in {round(seconds / 60)} minute(s)"
    elif seconds < 3600 * 24:
        readable = f"in {round(seconds / 3600)} hour(s)"
    elif seconds < 3600 * 24 * 7:
        readable = f"in {round(seconds / 3600 / 24)} day(s)"
    elif seconds < 3600 * 24 * 30:
        readable = f"in {round(seconds / 3600 / 24 / 7)} week(s)"
    elif seconds < 3600 * 24 * 365:
        readable = f"in {round(seconds / 3600 / 24 / 30)} month(s)"
    else:
        readable = f"in {round(seconds / 3600 / 24 / 365)} years(s)"

    return readable


class RecapMenu(Menu):
    def __init__(self, tk, manager):
        super(Menu, self).__init__()

        self.frame = Frame(tk, bg=shm.bg)

        self.title_l = Label(self.frame, text="Recap", font=font.en(20), fg=shm.fg, bg=shm.bg)
        self.title_l.place(x=20, y=20)

        self.title_l = Label(self.frame, text="Comming up next:", font=font.en(14), fg=shm.fg, bg=shm.bg)
        self.title_l.place(x=20, y=65)

        self.comming_up_l = []

        kanjis = Data.get_kanji_comming_up()
        for k, kj in enumerate(sorted(kanjis, key=lambda e: e.updated)):
            if k < 10:
                self.comming_up_l.append(
                    Label(self.frame, text=f"{Data.get_kanji_by_id(kj.id)[1]}, grade: {kj.memorised}, next {readable_time(kj.updated)}", font=font.jp(12), fg=shm.fg, bg=shm.bg)
                )
                self.comming_up_l[-1].place(x=20, y=90 + 30 * k)

        self.leave_b = Button(self.frame, text="leave", font=font.en(12), fg=shm.fg, bg=shm.bg, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.leave_b.place(x=20, y=405)

        # TODO: add button to add new kanji
