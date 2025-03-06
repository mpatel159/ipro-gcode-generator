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

        # print('hello world')
        container = tk.Frame(self)
        container.pack(fill='both', expand=1)
        # self.get_initial_data()

        self.listing = {}
        for p in (LandingPage, TubePage, NoseConePage):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
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

        to_tube = tk.Button(self, text="Tube", command=lambda: controller.up_frame("TubePage"))
        to_tube.pack()

        to_nose_cone = tk.Button(self, text="Nose Cone", command=lambda: controller.up_frame("NoseConePage"))
        to_nose_cone.pack()


class TubePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Tube Parameters", font=("Arial", 16)).pack(pady=10)

        self.inner_diameter = self.create_input_field("Inner Diameter (mm):")
        self.wall_thickness = self.create_input_field("Wall Thickness (mm):")
        self.length = self.create_input_field("Length (mm):")

        generate_btn = tk.Button(self, text="Generate G-Code", command=self.generate_gcode)
        generate_btn.pack(pady=10)

        self.gcode_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=15)
        self.gcode_display.pack(pady=10)

    def create_input_field(self, label_text):
        frame = tk.Frame(self)
        frame.pack(pady=5, padx=20, fill="x")

        tk.Label(frame, text=label_text, width=20, anchor="w").pack(side="left")
        entry = tk.Entry(frame, width=20)
        entry.pack(side="right")
        return entry

    def generate_gcode(self):
        try:
            inner_diameter = float(self.inner_diameter.get())
            wall_thickness = float(self.wall_thickness.get())
            length = float(self.length.get())

            if inner_diameter <= 0 or wall_thickness <= 0 or length <= 0:
                raise ValueError("All values must be greater than zero.")

            gcode = []
            gcode.append("G0 X0 Y0 Z0")
            gcode.append(f"G92 X{inner_diameter} Y{wall_thickness} Z{length}")
            gcode.append("; Layer 1")
            gcode.append(f"G1 X{inner_diameter + 1} Y{wall_thickness + 1} Z{length + 1} F1500")

            with open("output.gcode", "w") as f:
                f.write("\n".join(gcode))

            messagebox.showinfo("Success", "G-Code has been generated!")
            self.display_gcode()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def display_gcode(self):
        try:
            with open("output.gcode", "r") as f:
                gcode_content = f.read()
                self.gcode_display.delete("1.0", tk.END)
                self.gcode_display.insert(tk.END, gcode_content)
        except FileNotFoundError:
            messagebox.showerror("Error", "G-Code file not found. Make sure the script executed correctly.")


class NoseConePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Nose Cone Parameters", font=("Arial", 16)).pack(pady=10)

        self.geometry_type = self.create_input_field("Geometry Type:")
        self.thickness = self.create_input_field("Thickness (mm):")
        self.inner_diameter = self.create_input_field("Inner Diameter (mm):")
        self.length = self.create_input_field("Length (mm):")

        generate_btn = tk.Button(self, text="Generate G-Code", command=self.generate_gcode)
        generate_btn.pack(pady=10)

        self.gcode_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=15)
        self.gcode_display.pack(pady=10)

    def create_input_field(self, label_text):
        frame = tk.Frame(self)
        frame.pack(pady=5, padx=20, fill="x")

        tk.Label(frame, text=label_text, width=20, anchor="w").pack(side="left")
        entry = tk.Entry(frame, width=20)
        entry.pack(side="right")
        return entry

    def generate_gcode(self):
        try:
            geometry_type = self.geometry_type.get()
            thickness = float(self.thickness.get())
            inner_diameter = float(self.inner_diameter.get())
            length = float(self.length.get())

            if thickness <= 0 or inner_diameter <= 0 or length <= 0:
                raise ValueError("All values must be greater than zero.")

            gcode = []
            gcode.append("G0 X0 Y0 Z0")
            gcode.append(f"G92 X{inner_diameter} Y{thickness} Z{length}")
            gcode.append("; Layer 1")
            gcode.append(f"G1 X{inner_diameter + 1} Y{thickness + 1} Z{length + 1} F1500")

            with open("output.gcode", "w") as f:
                f.write("\n".join(gcode))

            messagebox.showinfo("Success", "G-Code has been generated!")
            self.display_gcode()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def display_gcode(self):
        try:
            with open("output.gcode", "r") as f:
                gcode_content = f.read()
                self.gcode_display.delete("1.0", tk.END)
                self.gcode_display.insert(tk.END, gcode_content)
        except FileNotFoundError:
            messagebox.showerror("Error", "G-Code file not found. Make sure the script executed correctly.")


if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()
