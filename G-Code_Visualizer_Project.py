import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

# Store coordinates
points_x = []
points_y = []


# Open GCODE file
def open_file():

    filepath = filedialog.askopenfilename(
        filetypes=[("GCODE Files", "*.gcode *.nc")]
    )

    if not filepath:
        return

    # Clear old data
    points_x.clear()
    points_y.clear()

    text_box.delete(1.0, tk.END)

    try:
        with open(filepath, "r") as file:
            lines = file.readlines()

        for line in lines:

            # Show code in text area
            text_box.insert(tk.END, line)

            # Find X and Y coordinates
            if "X" in line and "Y" in line:

                try:
                    x = float(line.split("X")[1].split()[0])
                    y = float(line.split("Y")[1].split()[0])

                    points_x.append(x)
                    points_y.append(y)

                except:
                    pass

        messagebox.showinfo(
            "Success",
            "File loaded successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# Draw tool path
def draw_path():

    if len(points_x) == 0:
        messagebox.showwarning(
            "Warning",
            "No coordinates found!"
        )
        return

    plt.figure(figsize=(6, 6))

    plt.plot(points_x, points_y, marker='o')

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.title("NC Tool Path Visualization")

    plt.grid(True)

    plt.show()


# Main window
root = tk.Tk()

root.title("Simple NC Viewer")

root.geometry("800x600")


# Buttons
open_button = tk.Button(
    root,
    text="Open GCODE File",
    command=open_file,
    height=2,
    width=20
)

open_button.pack(pady=10)

draw_button = tk.Button(
    root,
    text="Draw Tool Path",
    command=draw_path,
    height=2,
    width=20
)

draw_button.pack(pady=10)


# Text box
text_box = tk.Text(root)

text_box.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=10
)


# Run GUI
root.mainloop()