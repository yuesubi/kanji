
from tkinter import *


class DrawSurf:
    def __init__(self, master, **kwargs):
        self._canvas = Canvas(master, **kwargs)

        self._brush_col = "#FFF"

        self.is_drawing = False
        self._canvas.bind('<Button>', self._canvas_click_cmd)
        self._canvas.bind('<Motion>', self._canvas_motion_cmd)
        self._canvas.bind('<ButtonRelease>', self._canvas_release_cmd)

        self.brush_size = 4
        self.last_brush_pos = (0, 0)

    def place(self, **kwargs):
        self._canvas.place(**kwargs)

    def clear(self):
        self._canvas.delete('all')

    def _draw(self, x, y):
        self._canvas.create_oval(
            x - self.brush_size/2,
            y - self.brush_size/2,
            x + self.brush_size,
            y + self.brush_size,
            fill=self._brush_col, width=0 )

    def _canvas_click_cmd(self, evt):
        if evt.num == 1:
            self.is_drawing = True
            self._draw(evt.x, evt.y)
            self.last_brush_pos = evt.x, evt.y

    def _canvas_motion_cmd(self, evt):
        if self.is_drawing:
            curr_pos = evt.x, evt.y
            motion = curr_pos[0] - self.last_brush_pos[0], curr_pos[1] - self.last_brush_pos[1]
            abs_motion = ( abs(curr_pos[0] - self.last_brush_pos[0]),
                abs(curr_pos[1] - self.last_brush_pos[1]) )

            if abs_motion[0] < 2 and abs_motion[1] < 2:
                self._draw(evt.x, evt.y)
            else:
                side = (0 if abs_motion[0] == 0 else motion[0] / abs_motion[0],
                    0 if abs_motion[1] == 0 else motion[1] / abs_motion[1])

                if abs_motion[0] > abs_motion[1]:
                    for x in range(abs_motion[0]):
                        divzero = 0 if abs_motion[0] == 0 else motion[1] / abs_motion[0]
                        self._draw( curr_pos[0] + int(x * side[0]),
                            curr_pos[1] + int(divzero * x) )
                else:
                    for y in range(abs_motion[1]):
                        divzero = 0 if abs_motion[1] == 0 else motion[0] / abs_motion[1]
                        self._draw( curr_pos[0] + int(divzero * y),
                            curr_pos[1] + int(y * side[1]) )

            self.last_brush_pos = curr_pos

    def _canvas_release_cmd(self, evt):
        if evt.num == 1:
            self.is_drawing = False
