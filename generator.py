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

        button_frame = tk.Frame(self)
        button_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        to_tube = tk.Button(button_frame, text="Tube", command=lambda: controller.up_frame("TubePage"))
        to_tube.pack(pady=5)
        
        to_nose_cone = tk.Button(button_frame, text="Nose Cone", command=lambda: controller.up_frame("NoseConePage"))
        to_nose_cone.pack(pady=5)

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
        content_frame = tk.Frame(self)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        label = tk.Label(content_frame, text="Nose Cone")
        label.pack(pady=5)

        # User can choose what kind of nose cone geometry they want to use.
        geo_label = tk.Label(content_frame, text="What geometry do you want")
        geo_label.pack(pady=5)
        nose_cone_options = ['Von Karman', 'Tangent Ogive']
        clicked = tk.StringVar()  # variable that stores what option user chose
        clicked.set(nose_cone_options[0])  # set it to the first option (Von Karman)
        drop = tk.OptionMenu(content_frame, clicked, *nose_cone_options)
        drop.pack(pady=5)

        def validate_number(P):
            # Allow empty input, otherwise try converting to float.
            if P == "":
                return True
            try:
                float(P)
                return True
            except ValueError:
                return False

        # Setup validation for numeric input.
        vcmd = (self.register(validate_number), '%P')

        # Thickness Entry
        thickness_label = tk.Label(content_frame, text="Thickness")
        thickness_label.pack(pady=5)
        thickness_entry = tk.Entry(content_frame, width=10, validate="key", validatecommand=vcmd)
        thickness_entry.pack(pady=5)

        # Inner Diameter Entry
        inner_diameter_label = tk.Label(content_frame, text="Inner Diameter")
        inner_diameter_label.pack(pady=5)
        inner_diameter_entry = tk.Entry(content_frame, width=10, validate="key", validatecommand=vcmd)
        inner_diameter_entry.pack(pady=5)

        # Nose Cone Length Entry
        length_label = tk.Label(content_frame, text="Length")
        length_label.pack(pady=5)
        length_entry = tk.Entry(content_frame, width=10, validate="key", validatecommand=vcmd)
        length_entry.pack(pady=5)

        save_button = tk.Button(content_frame, text="Save", command=lambda: save_to_file())
        save_button.pack(pady=10)

        def save_to_file():
            data = {
                "Geometry": clicked.get(),
                "Thickness": thickness_entry.get(),
                "Inner Diameter": inner_diameter_entry.get(),
                "Length": length_entry.get()
            }
            with open("nose_cone.json", "w") as file:
                json.dump(data, file, indent=4)
            # file = open("nose_cone.txt", "w")
            # file.write('Geometry: ' + str(clicked.get()) + "\n")
            # file.write('Thickness: ' + str(thickness.get("1.0", "end-1c")) + "\n")
            # file.write('Inner Diameter: ' + str(inner_diameter.get("1.0", "end-1c")) + "\n")
            # file.write('Length: ' + str(length.get("1.0", "end-1c")) + "\n")








if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()