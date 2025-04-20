import tkinter as tk
from logic.simulation import start_simulation
from logic.matrix import update_canvas, zoom

def add_controls(left_frame, canvas, entries, elements):
    tk.Label(left_frame, text="Controls", bg="#eee", font=("Arial", 14)).pack(pady=10)

    for label, default in [("Cell Size:", 5), ("Rows:", 125), ("Columns:", 125)]:
        tk.Label(left_frame, text=label, bg="#eee").pack(pady=(10, 0))
        entry = tk.Entry(left_frame)
        entry.insert(0, str(default))
        entry.pack()
        entries.append(entry)

    tk.Button(left_frame, text="Zoom In", command=lambda: zoom(canvas, 2, entries)).pack(pady=(10, 0))
    tk.Button(left_frame, text="Zoom Out", command=lambda: zoom(canvas, -2, entries)).pack()
    tk.Button(left_frame, text="Start Simulation", command=lambda: start_simulation(canvas, entries, elements)).pack(pady=20)
    update_canvas(canvas, entries)
