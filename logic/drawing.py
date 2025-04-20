import math

def draw_matrix(canvas, matrix, cell_size):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            dist = math.sqrt(row**2 + col**2)
            color = "black" if abs(dist - rows) < 0.4 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    canvas.config(scrollregion=(0, 0, cols * cell_size, rows * cell_size))
