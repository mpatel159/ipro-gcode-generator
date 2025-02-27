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

class NoseConePage(tk.Frame):  # Nose cone page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Nose Cone")
        label.pack()

        #user can choose what kind of nose cone geometry they want to use
        label = tk.Label(self, text="What geometry do you want")
        label.pack()
        nose_cone_options = ['Von Karman', 'Tangent Ogive']
        clicked = tk.StringVar() #variable that stores what option user chose
        clicked.set(nose_cone_options[0]) #set it to the first option (Von Karman)
        drop = tk.OptionMenu( self , clicked , *nose_cone_options ) #creates the dropdown
        drop.pack()

        #Choosing Thickness section
        label = tk.Label(self, text="Thickness")
        label.pack()
        thickness = tk.Text(self, width=10, height=1)
        thickness.pack()

        #inner diameter section
        label = tk.Label(self, text="Inner diameter")
        label.pack()
        inner_diameter = tk.Text(self, width=10, height=1)
        inner_diameter.pack()

        #Nose cone length section
        label = tk.Label(self, text="Length")
        label.pack()
        length = tk.Text(self, width=10, height=1)
        length.pack()

        save_button = tk.Button(self, text="Save", command=lambda: save_to_file())
        save_button.pack()

        def save_to_file():
            file = open("nose_cone.txt", "w")
            file.write('Geometry: ' + str(clicked.get()) + "\n")
            file.write('Thickness: ' + str(thickness.get("1.0", "end-1c")) + "\n")
            file.write('Inner Diameter: ' + str(inner_diameter.get("1.0", "end-1c")) + "\n")
            file.write('Length: ' + str(length.get("1.0", "end-1c")) + "\n")








if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()