import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validate_weight_input(text):
    return text.replace('.', '', 1).isdigit() or text == ''

def calculate_dosage():
    try:
        weight_unit = unit_combobox.get()
        if weight_unit.lower() not in ["kg", "lbs", "grams"]:
            raise ValueError("Invalid unit. Please enter a valid unit from the drop-down list (kg/lbs/grams).")
        
        weight_input = weight_entry.get().strip()
        if not weight_input:
            raise ValueError("Weight field is empty. Please enter the patient's weight.")
        
        if not validate_weight_input(weight_input):
            raise ValueError("Invalid weight input. Please enter a numeric value.")
        
        weight_input = float(weight_entry.get())
        weight = convert_to_kilograms(weight_input, weight_unit)

        if weight < 0:
            raise ValueError("Weight must be a positive value.")
        
        weight = convert_to_kilograms(weight_input, weight_unit)
        
        result = calculate(weight)
        result_var.set("The calculated dosage is: {:.2f}".format(result))

        weight_entry.delete(0, tk.END)
        unit_combobox.set("")

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

def handle_enter_key(event):
    calculate_dosage()
    
window = tk.Tk()
window.title("Dosage Calculator")

style = ttk.Style()

style.configure("RoundedEntry.TEntry", borderwidth=0, relief="solid", fieldbackground="#FFFFFF", bordercolor="#A9A9A9",
                foreground="#000000", font=("Helvetica", 12))

style.configure("RoundedButton.TButton", borderwidth=0, relief="solid", background="#007AFF", foreground="#FFFFFF", 
                font=("Helvetica", 12), padx=10, pady=5)

weight_label = tk.Label(window, text="Enter the patient's weight:")
weight_label.pack()
weight_entry = ttk.Entry(window, style="RoundedEntry.TEntry")
weight_entry.pack(pady=5)

validate_weight = window.register(validate_weight_input)
weight_entry.configure(validate="key", validatecommand=(validate_weight, '%P'))

unit_label = tk.Label(window, text="Select the unit of weight:")
unit_label.pack()

unit_combobox = ttk.Combobox(window, values=["kg", "lbs", "grams"])
unit_combobox.pack(pady=5)

calculate_button = ttk.Button(window, text="Calculate", command=calculate_dosage, style="RoundedButton.TButton")
calculate_button.pack(pady=10)

style.map("RoundedButton.TButton",
          background=[("active", "#007AFF"), ("!active", "SystemButtonFace")],
          foreground=[("active", "#FFFFFF"), ("!active", "SystemButtonText")])


result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var)   
result_label.pack()

unit_combobox.configure(state="readonly")

result_var.set("")

window.bind("<Return>", handle_enter_key)

window.mainloop()
