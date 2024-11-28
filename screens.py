import tkinter as tk
from tkinter import ttk
from utils import get_text

class MainScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()
        style.theme_use("clam")

        self.postcode = ""

        self.address_entry_label = ttk.Label(self, text="what the sigma main screen?!\nenter your home postcode buddy")
        self.address_entry = ttk.Entry(self)

        self.address_entry_label.pack(pady=20)
        self.address_entry.pack(pady=20)
        self.address_entry.focus()
        self.address_entry.bind("<Return>", self.get_postcode)

    def get_postcode(self, event):
        self.postcode = self.address_entry.get()
        print(self.postcode)