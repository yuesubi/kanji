# -*- encode: utf-8 -*-

import os
import time
from tkinter import *

from menu import Menu
from widgets.draw_surf import DrawSurf
from data import Data, Kanji

import res.assets as assets
import res.font as font
import res.shm as shm


class ExamMenu(Menu):
    def __init__(self, tk, manager):
        super(Menu, self).__init__()
        self.manager = manager

        self.frame = Frame(tk, bg=shm.bg)

        self.title_l = Label(self.frame, text="Draw the kanji of:", font=font.en(20), fg=shm.fg, bg=shm.bg)
        self.title_l.place(x=20, y=20)

        self.draw_d = DrawSurf(self.frame, width=235, height=235, bg=shm.bg)
        self.draw_d.place(x=20, y=155)

        self.answer_kanji_l = Label(self.frame, text=" ", font=font.jp(120), fg=shm.fg, bg=shm.bg)
        self.answer_kanji_l.place(x=270, y=155)

        self.kuns =   []
        self.ons =    []
        self.sounds = []

        # Bottom buttons
        self.leave_b = Button(self.frame, text="leave", font=font.en(12), fg=shm.fg, bg=shm.bg, command=lambda: manager.switch("entry_menu"), relief='flat')
        self.leave_b.place(x=20, y=405)

        self.erase_b = Button(self.frame, text="erase", font=font.en(12), fg=shm.fg, bg=shm.bg, command=self.draw_d.clear, relief='flat')
        self.erase_b.place(x=120, y=405)

        self.check_b = Button(self.frame, text="check", font=font.en(12), fg=shm.fg, bg=shm.bg, command=self.load_answer, relief='flat')
        self.check_b.place(x=220, y=405)

        self.wrong_b = Button(self.frame, text="wrong", font=font.en(12), fg=shm.fg, bg=shm.bg, command=self.wrong, relief='flat')
        self.wrong_b.place(x=320, y=405)

        self.correct_b = Button(self.frame, text="correct", font=font.en(12), fg=shm.fg, bg=shm.bg, command=self.correct, relief='flat')
        self.correct_b.place(x=400, y=405)

        self.questions  = Data.get_kanji_to_see()
        
        if f"{time.asctime().split(sep=' ')[1]} {time.asctime().split(sep=' ')[2]}" != Data.get_last_time():
            self.questions.extend( Data.get_new_kanji(2) )

        if len(self.questions) == 0:
            self.manager.switch("recap_menu")
            return

        self.curr_kanji = Data.get_kanji_by_id(self.questions[0].id)

        self.curr_question = {
            "kun": self.curr_kanji[4],
            "on" : self.curr_kanji[3]
        }
        self.curr_answer   = {
            "kanji" : self.curr_kanji[1],
            "sounds": self.curr_kanji[2],
        }

        self.achivements = list()
        self.quest_num = 0

        self.load_question()

    def load_next_question(self):
        self.quest_num += 1

        if not (self.quest_num < len(self.questions)):
            self.finish()
            return

        self.curr_kanji = Data.get_kanji_by_id(self.questions[self.quest_num].id)

        self.curr_question = {
            "kun": self.curr_kanji[4],
            "on" : self.curr_kanji[3]
        }
        self.curr_answer   = {
            "kanji" : self.curr_kanji[1],
            "sounds": self.curr_kanji[2],
        }

        self.answer_kanji_l.config(text=' ')
        self.draw_d.clear()

        self.load_question()

        self.check_b.config(state='normal')

    def finish(self):
        Data.save_achivements(self.achivements)
        Data.save_time()
        self.manager.switch("recap_menu")

    def correct(self):
        self.achive(1)
        self.load_next_question()

    def wrong(self):
        self.achive(-1)
        self.load_next_question()

    def achive(self, mem_added, known=False):
        kj = self.questions[self.quest_num]
        self.achivements.append(
            Kanji(kj.id, int(time.time()), max(0, kj.memorised + mem_added), known)
        )

    def load_question(self):
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
        for k, kun in enumerate(self.curr_question["kun"].split(sep='; ')):
            self.kuns.append(
                Label(self.frame, text=kun, font=font.en(12), fg=shm.fg, bg=shm.bg)
            )
            self.kuns[-1].place(x=20, y=70 + 30 * k)

        
        # Translation of the on readings
        for o, on in enumerate(self.curr_question["on"].split(sep='; ')):
            self.ons.append(
                Label(self.frame, text=on, font=font.en(12), fg=shm.comment, bg=shm.bg)
            )
            self.ons[-1].place(x=320, y=70 + 30 * o)

        self.wrong_b.config(state='disabled')
        self.correct_b.config(state='disabled')

    def load_answer(self):
        # Kanji
        self.answer_kanji_l.config(text=self.curr_answer["kanji"])

        # Prononciation
        for s, sound in enumerate(self.curr_answer["sounds"].split(sep='、')):
            self.sounds.append(
                Label(self.frame, text=sound, font=font.jp(16), fg=shm.fg, bg=shm.bg)
            )
            self.sounds[-1].place(x=450, y=155 + 40 * s)

        
        self.wrong_b.config(state='normal')
        self.correct_b.config(state='normal')
        
        self.check_b.config(state='disabled')


#         self.known_b = Button(self.button_f, text="known", font=font(14), bd=0, highlightthickness=0)
#         self.known_b.grid(row=0, column=4, padx=(20, 0), pady=(5, 0), sticky='e')