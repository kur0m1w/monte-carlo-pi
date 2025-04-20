import numpy as np
import random
from logic.drawing import draw_matrix

def in_circle(x, y, rows):
    return (x**2 + y**2)**0.5 < rows

def update_info(b, r, elements):
    elements[0].config(text=f"r = {r}")
    elements[1].config(text=f"b = {b}")
    elements[2].config(text=f"n = r + b = {r+b}")

def start_simulation(canvas, entries, elements):
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

    b = 0
    r = 0

    x_data = []
    y_data = []

    def step(b, r):
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        matrix[y][x] = 1
        x1, y1 = x * cell_size, y * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        if in_circle(x, y, rows):
            color = "red"
            r += 1
        else:
            color = "blue"
            b += 1
        update_info(b, r, elements)

        if r != 0 and b != 0:
            x_data.append(r+b)
            y_data.append(4*r/(r+b))

            elements[3].set_data(x_data, y_data)
            elements[3].axes.relim()            
            elements[3].axes.autoscale_view() 
            elements[4].draw()    
            elements[5].set_text(r"$\pi \approx \frac{4 \times %d}{%d} = %.6f$" % (r, r+b, 4*r/(r+b)))

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
        canvas.config(scrollregion=(0, 0, cols * cell_size, rows * cell_size))
        canvas.after(50, lambda: step(b, r))

    step(b, r)
