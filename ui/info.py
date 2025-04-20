import tkinter as tk
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

def add_info(bottom_right_frame):
    elements = []

    bottom_right_frame.grid_columnconfigure(0, weight=1)
    bottom_right_frame.grid_columnconfigure(1, weight=1)
    bottom_right_frame.grid_rowconfigure(0, weight=1)

    left_frame = tk.Frame(bottom_right_frame, bg="white")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = tk.Frame(bottom_right_frame, bg="#ccc")
    right_frame.grid(row=0, column=1, sticky="nsew")

    r_count = tk.Label(left_frame, text="r = 0", font=("Arial", 12), anchor="w")
    r_count.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    b_count = tk.Label(left_frame, text="b = 0", font=("Arial", 12), anchor="w")
    b_count.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    n_count = tk.Label(left_frame, text="n = r + b = 0", font=("Arial", 12), anchor="w")
    n_count.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    elements.append(r_count)
    elements.append(b_count)
    elements.append(n_count)

    width = 100
    height = 20
    x_range = (0, 100)
    y_range = (-5, 5)

    fig = Figure(figsize=(5, 2), dpi=100)
    plot = fig.add_subplot(111)
    plot.set_ylim(math.pi - 2, math.pi + 2)
    line, = plot.plot([], [], label="r / b")
    plot.grid(True)
    plot.axhline(y=math.pi, color='black', linewidth=1)
    plot.legend()
    plot.set_yticks([0, math.pi, 6])
    plot.set_yticklabels([r"0", r"$\pi$", r"6"])
    plot.set_xlim(auto=True)
    plot_text = plot.text(
    0.05, 0.95,
    r"$\pi \approx \frac{4 \times r}{n} = %.6f$" % 0,
    transform=plot.transAxes,
    fontsize=14,
    verticalalignment='top')


    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    elements.append(line)
    elements.append(canvas)
    elements.append(plot_text)

    return elements