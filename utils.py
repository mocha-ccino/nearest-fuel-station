import tkinter as tk
from tkinter import ttk

def get_screen_dimensions():
    dummy = tk.Tk()
    dummy.tk.call('tk', 'scaling', 1.0)
    height = dummy.winfo_screenheight()
    width = dummy.winfo_screenwidth()
    dummy.destroy()
    return [width, height]

def get_text(event):
    widget = event.widget
    return widget.get()