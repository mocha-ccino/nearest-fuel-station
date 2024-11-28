import tkinter as tk
from tkinter import ttk
import pyautogui

def get_screen_dimensions():
    size = pyautogui.size()
    return (size[0], size[1])

def get_text(event):
    widget = event.widget
    return widget.get()