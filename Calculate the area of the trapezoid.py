import tkinter as tk


def calculate_area():
    # Retrieve the input values from the entry widgets
    base1 = float(base1_entry.get())
    base2 = float(base2_entry.get())
    height = float(height_entry.get())

    # Calculate the area of the trapezoid
    area = (base1 + base2) * height / 2

    # Update the label widget to display the area
    result_label.config(text=f"The area of the trapezoid is {area:.2f} units.")

# Create the main window
root = tk.Tk()
root.title("Trapezoid Area Calculator")

# Create the input widgets
base1_label = tk.Label(root, text="Base 1")
base1_label.grid(row=0, column=0)

base1_entry = tk.Entry(root)
base1_entry.grid(row=0, column=1)

base2_label = tk.Label(root, text="Base 2")
base2_label.grid(row=1, column=0)

base2_entry = tk.Entry(root)
base2_entry.grid(row=1, column=1)

height_label = tk.Label(root, text="Height")
height_label.grid(row=2, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1)

# Create the button widget
calculate_button = tk.Button(root, text="Calculate", command=calculate_area)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create the label widget
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
