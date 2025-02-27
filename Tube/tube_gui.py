import subprocess
import json
import tkinter as tk
from tkinter import messagebox

# 创建 GUI 界面
root = tk.Tk()
root.title("Filament Winder - Tube Design")
root.geometry("400x250")

# 添加输入框和标签
tk.Label(root, text="Inner Diameter (mm):").grid(row=0, column=0, padx=10, pady=5)
inner_diameter_entry = tk.Entry(root)
inner_diameter_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Wall Thickness (mm):").grid(row=1, column=0, padx=10, pady=5)
wall_thickness_entry = tk.Entry(root)
wall_thickness_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Length (mm):").grid(row=2, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1, padx=10, pady=5)

# **修改 submit() 让其自动调用 `cli-entry.js`**
def submit():
    try:
        # **获取用户输入并转换成数值**
        inner_diameter = float(inner_diameter_entry.get())
        wall_thickness = float(wall_thickness_entry.get())
        length = float(length_entry.get())

        # **检查输入是否合法**
        if inner_diameter <= 0 or wall_thickness <= 0 or length <= 0:
            raise ValueError("All values must be greater than zero.")

        # **创建 JSON 数据**
        input_data = {
            "type": "tube",
            "inner_diameter": inner_diameter,
            "wall_thickness": wall_thickness,
            "length": length,
            "feed_rate": 1500
        }

        # **保存 JSON 数据到 input.json**
        with open("input.json", "w") as f:
            json.dump(input_data, f, indent=4)

        # **调用 Node.js 运行 `cli-entry.js`**
        result = subprocess.run(["node", "cli-entry.js", "input.json"], capture_output=True, text=True)

        if result.returncode == 0:
            messagebox.showinfo("Success", "✅ GCode has been generated: output.gcode!")
        else:
            messagebox.showerror("Error", f"❌ Failed to generate GCode:\n{result.stderr}")

    except ValueError:
        messagebox.showerror("Error", "❌ Please enter valid numbers!")

# **添加按钮**
submit_button = tk.Button(root, text="Generate GCode", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# **运行 Tkinter 主循环**
root.mainloop()
