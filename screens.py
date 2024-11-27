import tkinter as tk
from tkinter import ttk
style = ttk.Style()
style.theme_use("clam")

class MainScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        address_entry_label = ttk.Label(self, text="what the sigma main screen?!\nenter your home postcode buddy")
        address_entry = ttk.Entry()

        address_entry_label.pack(pady=20)
        address_entry.pack(pady=20)
        address_entry.focus()