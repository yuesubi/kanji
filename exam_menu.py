# -*- encode: utf-8 -*-

from tkinter import *

from menu import Menu
from widgets.draw_surf import DrawSurf

import res.assets as assets
import res.font as font
import res.shm as shm


class ExamMenu(Menu):
    def __init__(self, tk, manager):
        super(Menu, self).__init__()

        self.frame = Frame(tk, bg=shm.bg)

        self.title_l = Label(self.frame, text="Draw the kanji of:", font=font.en(20), fg=shm.fg, bg=shm.orange)
        self.title_l.place(x=20, y=20)

        self.draw_d = DrawSurf(self.frame, width=235, height=235, bg=shm.orange)
        self.draw_d.place(x=20, y=155)

        self.answer_kanji_l = Label(self.frame, text=" ", font=font.jp(120), fg=shm.fg, bg=shm.orange)
        self.answer_kanji_l.place(x=270, y=155)

        self.kuns =   []
        self.ons =    []
        self.sounds = []

        # Bottom buttons
        self.leave_b = Button(self.frame, text="leave", font=font.en(12), fg=shm.fg, bg=shm.orange, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.leave_b.place(x=20, y=405)

        self.erase_b = Button(self.frame, text="erase", font=font.en(12), fg=shm.fg, bg=shm.orange, command=lambda: self.draw_d.clear(), relief='flat')
        self.erase_b.place(x=120, y=405)

        self.check_b = Button(self.frame, text="check", font=font.en(12), fg=shm.fg, bg=shm.orange, command=lambda: self.load_answer(), relief='flat')
        self.check_b.place(x=220, y=405)

        self.wrong_b = Button(self.frame, text="wrong", font=font.en(12), fg=shm.fg, bg=shm.orange, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.wrong_b.place(x=320, y=405)

        self.correct_b = Button(self.frame, text="correct", font=font.en(12), fg=shm.fg, bg=shm.orange, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.correct_b.place(x=400, y=405)

        self.load_question()

    def load_question(self):
        question = {
            "kun": "moon; month",
            "on": "moon; month; Monday; month (of the year)",
        }

        # Clear the prononciatiobns of the kanji
        for sound in self.sounds:
            sound.place_forget()
        self.sounds.clear()
        # Clear of the kun
        for kun in self.kuns:
            kun.place_forget()
        self.kuns.clear()
        # Clear of the on
        for on in self.ons:
            on.place_forget()
        self.ons.clear()

        # Translation of the kun readings
        for k, kun in enumerate(question["kun"].split(sep='; ')):
            self.kuns.append(
                Label(self.frame, text=kun, font=font.en(12), fg=shm.fg, bg=shm.orange)
            )
            self.kuns[-1].place(x=20, y=70 + 30 * k)

        
        # Translation of the on readings
        for o, on in enumerate(question["on"].split(sep='; ')):
            self.ons.append(
                Label(self.frame, text=on, font=font.en(12), fg=shm.comment, bg=shm.orange)
            )
            self.ons[-1].place(x=320, y=70 + 30 * o)

    def load_answer(self):
        answer = {
            "kanji": '月',
            "sounds": "ゲツ、ガツ、つき",
        }
        
        # Kanji
        self.answer_kanji_l.config(text=answer["kanji"])

        # Prononciation
        for s, sound in enumerate(answer["sounds"].split(sep='、')):
            self.sounds.append(
                Label(self.frame, text=sound, font=font.jp(16), fg=shm.fg, bg=shm.orange)
            )
            self.sounds[-1].place(x=450, y=155 + 40 * s)


#         self.known_b = Button(self.button_f, text="known", font=font(14), bd=0, highlightthickness=0)
#         self.known_b.grid(row=0, column=4, padx=(20, 0), pady=(5, 0), sticky='e')