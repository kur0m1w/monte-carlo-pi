import numpy as np
import tkinter as tk
from logic.drawing import draw_matrix

def update_canvas(canvas, entries):
    try:
        cell_size = int(entries[0].get())
        rows = int(entries[1].get())
        cols = int(entries[2].get())
    except ValueError:
        print("Invalid input")
        return

    matrix = np.zeros((rows, cols))
    canvas.delete("all")
    draw_matrix(canvas, matrix, cell_size)

def zoom(canvas, factor, entries):
    try:
        current = int(entries[0].get())
        new_size = max(1, current + factor)
        entries[0].delete(0, tk.END)
        entries[0].insert(0, str(new_size))
        update_canvas(canvas, entries)
    except ValueError:
        print("Invalid input")
