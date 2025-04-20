import tkinter as tk

def setup_layout(root):
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)

    left_frame = tk.Frame(root, bg="#eee")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew")

    right_frame.grid_rowconfigure(0, weight=3)
    right_frame.grid_rowconfigure(1, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    top_right_frame = tk.Frame(right_frame, bg="white")
    top_right_frame.grid(row=0, column=0, sticky="nsew")

    bottom_right_frame = tk.Frame(right_frame, bg="#ccc")
    bottom_right_frame.grid(row=1, column=0, sticky="nsew")

    canvas_container = tk.Frame(top_right_frame)
    canvas_container.pack(fill="both", expand=True)
    canvas_container.grid_rowconfigure(0, weight=1)
    canvas_container.grid_columnconfigure(0, weight=1)

    canvas = tk.Canvas(canvas_container, bg="white")
    canvas.grid(row=0, column=0, sticky="nsew")

    v_scroll = tk.Scrollbar(canvas_container, orient="vertical", command=canvas.yview)
    v_scroll.grid(row=0, column=1, sticky="ns")

    h_scroll = tk.Scrollbar(canvas_container, orient="horizontal", command=canvas.xview)
    h_scroll.grid(row=1, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

    entries = []
    return left_frame, top_right_frame, bottom_right_frame, canvas, entries