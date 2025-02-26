#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import math


class MainFrame(tk.Tk):
    cont = None
    def __init__(self, *args, **kwargs):
       # super().__init__()
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Test")
        self.geometry("800x700")
        
      #  print('hello world')
        container = tk.Frame(self)
        container.pack(fill='both', expand=1)
       # self.get_initial_data()

        self.listing = {}
        for p in (LandingPage, TubePage, NoseConePage) :
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.place(relheight=1, relwidth=1)
            self.listing[page_name] = frame
        self.up_frame('LandingPage')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
        
class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        to_tube = tk.Button(self, text = "Tube", command=lambda: controller.up_frame("TubePage"))
        to_tube.pack()

        to_nose_cone = tk.Button(self, text = "Nose Cone", command=lambda: controller.up_frame("NoseConePage"))
        to_nose_cone.pack()

class TubePage(tk.Frame):  # Inherit from tk.Frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tube")
        label.pack()

class NoseConePage(tk.Frame):  # Inherit from tk.Frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Nose Cone")
        label.pack()



if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()