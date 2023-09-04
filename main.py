import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("350x150")
window.title("Inches to Feet Calc")

def calculate_inches_to_feet():
    grab_unit_in_inches = int(unit_entry.get())
    convert_inches_to_feet = grab_unit_in_inches * 12
    messagebox.showinfo("Conversion", f"{grab_unit_in_inches} inches = {convert_inches_to_feet} feet")

unit_label = tk.Label(
    text = "Enter unit in inches here",
    bg = "black",
    fg = "white",
)

unit_entry = tk.Entry()

conversion_button = tk.Button(
    text = "Calculate units to feet",
    width = 15,
    height = 2,
    command = calculate_inches_to_feet
)

unit_label.pack()
unit_entry.pack()
conversion_button.pack()

window.mainloop()