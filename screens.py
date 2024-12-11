import tkinter as tk
from tkinter import ttk
from utils import get_text
import re


class MainScreen(tk.Frame):
    def __init__(self, parent, show_results_screen):
        super().__init__(parent)

        style = ttk.Style()
        style.theme_use("clam")

        self.postcode = ""
        self.show_results_screen = show_results_screen

        self.address_entry_label = ttk.Label(
            self, text="what the sigma main screen?!\nenter your home postcode buddy"
        )
        self.address_entry = ttk.Entry(self)
        self.feedback_label = ttk.Label(
            self, text="", foreground="red"
        )  # feedback for invalid input

        self.address_entry_label.pack(pady=20)
        self.address_entry.pack(pady=20)
        self.feedback_label.pack(pady=10)

        self.address_entry.focus()
        self.address_entry.bind("<Return>", self.get_postcode)

    def validate_postcode(self, value):
        """
        validate postcode input using a regex pattern.
        only allow valid uk postcodes (basic validation).
        """
        pattern = r"^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s?\d[A-Za-z]{2}$"
        return bool(re.match(pattern, value))

    def get_postcode(self, event):
        self.postcode = self.address_entry.get()

        # validate input
        if self.validate_postcode(self.postcode):
            self.feedback_label.config(
                text="you go bestie!", foreground="green"
            )  # clear feedback
            print(f"valid postcode: {self.postcode}")

            self.show_results_screen(self.postcode)
        else:
            self.feedback_label.config(
                text="invalid postcode! please try again.", foreground="red"
            )
            print("invalid postcode! please try again.")


class ResultsScreen(tk.Frame):
    def __init__(self, parent, postcode):
        super().__init__(parent)

        ttk.Label(self, text=f"results for: {postcode}").pack(pady=20)
        ttk.Button(
            self,
            text="back",
            command=lambda: parent.show_frame(MainScreen, parent.show_results_screen),
        ).pack(pady=10)
