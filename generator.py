#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import math


class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test")
        self.geometry("800x700")
        self.create_widgets()    
    
    def create_widgets(self):
        print('hello world')
        


if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()