import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validate_weight_input(text):
    return text.replace('.', '', 1).isdigit() or text == ''

def calculate_dosage():
    try:
        weight_unit = unit_combobox.get()
        if weight_unit.lower() not in ["kg", "lbs", "grams"]:
            raise ValueError("Invalid unit. Please enter a valid unit in (kg/lbs/grams).")
        
        weight_input = float(weight_entry.get())
        weight = convert_to_kilograms(weight_input, weight_unit)

        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        
        result = calculate(weight)
        result_var.set("The calculated dosage is: {:.2f}".format(result))

    except ValueError as error:
        messagebox.showerror("Error", str(error))

def convert_to_kilograms(weight, unit):
    if unit == "lbs":
        return weight * 0.45359237
    elif unit == "grams":
        return weight * 0.001
    else:
        return weight

def calculate(weight):
    dosage = weight * 0.1
    return dosage
    
window = tk.Tk()
window.title("Dosage Calculator")

weight_label = tk.Label(window, text="Enter the patient's weight:")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

validate_weight = window.register(validate_weight_input)
weight_entry.configure(validate="key", validatecommand=(validate_weight, '%P'))

unit_label = tk.Label(window, text="Select the unit of weight:")
unit_label.pack()
unit_combobox = ttk.Combobox(window, values=["kg", "lbs", "grams"])
unit_combobox.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_dosage)
calculate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var)   
result_label.pack()

unit_combobox.configure(state="readonly")

window.mainloop()