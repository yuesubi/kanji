# -*- encode: utf-8 -*-

from tkinter import *

from menu import Menu
from widgets.draw_surf import DrawSurf

import res.assets as assets
import res.font as font
import res.shm as shm


class ExamMenu(Menu):
    def __init__(self, tk):
        super(Menu, self).__init__()

        self.frame = Frame(tk, bg=shm.bg)

        self.title_l = Label(self.frame, text="Draw the kanji of: the moon", font=font.en(20), fg=shm.fg, bg=shm.orange)
        self.title_l.place(x=20, y=20)

        self.draw_d = DrawSurf(self.frame, width=235, height=235, bg=shm.orange)
        self.draw_d.place(x=20, y=70)

        self.answer_kanji_l = Label(self.frame, text="月", font=font.jp(120), fg=shm.fg, bg=shm.orange)
        self.answer_kanji_l.place(x=270, y=70)

        self.start_b = Button(self.frame, image=PhotoImage(file=assets.leave), fg=shm.fg, bg=shm.orange)  # , relief='flat')
        self.start_b.place(x=20, y=370)


#         self.known_b = Button(self.button_f, text="known", font=font(14), bd=0, highlightthickness=0)
#         self.known_b.grid(row=0, column=4, padx=(20, 0), pady=(5, 0), sticky='e')