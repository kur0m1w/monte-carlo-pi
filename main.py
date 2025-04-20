import tkinter as tk
from ui.layout import setup_layout
from ui.controls import add_controls
from ui.info import add_info

def main():
    root = tk.Tk()
    root.title("Matrix Viewer")
    root.geometry("825x1000")

    left_frame, top_right_frame, bottom_right_frame, canvas, entries = setup_layout(root)
    elements = add_info(bottom_right_frame)
    add_controls(left_frame, canvas, entries, elements)


    root.mainloop()

if __name__ == "__main__":
    main()
