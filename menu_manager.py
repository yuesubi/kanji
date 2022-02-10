# -*- encode: utf-8 -*-

from typing import Any

# from menu import Menu
from entry_menu import EntryMenu
from exam_menu import ExamMenu
from recap_menu import RecapMenu


MENUS_MAP: dict[str, Any] = {
    "entry_menu": EntryMenu,
    "exam_menu": ExamMenu,
    "recap_menu": RecapMenu
}


class Manager:
    _tk: Any = None
    _curr_menu = None

    @classmethod
    def init(cls, tk, first_menu: str):
        cls._tk = tk
        cls.switch(first_menu)

    @classmethod
    def switch(cls, menu: str) -> None:
        if cls._curr_menu is not None:
            cls._curr_menu.quit()
            cls._curr_menu.frame.place_forget()

        cls._curr_menu = MENUS_MAP[menu](cls._tk, cls)
        cls._curr_menu.frame.place(x=0, y=0, width=640, height=460)