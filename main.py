import tkinter as tk
from tkinter import ttk
import math
from utils import get_screen_dimensions
from screens import MainScreen
from db_updater import db_refesher

from typing import Callable


db_refesher()
screen_dimensions = get_screen_dimensions()
window_dimensions = [math.floor(x * 0.82) for x in screen_dimensions]

def show_frame(container: tk.Frame, frame_class) -> None:
    """Destroy the current frame and replace it with a new one."""
    for widget in container.winfo_children():
        widget.destroy()

    frame = frame_class(container)   
    frame.pack(fill="both")

def main():
    root = tk.Tk()
    root.geometry(f"{window_dimensions[0]}x{window_dimensions[1]}")
    root.title("Fast Fuel Finder")

    show_frame(root, MainScreen)

    root.mainloop()

if __name__ == "__main__":
    main()