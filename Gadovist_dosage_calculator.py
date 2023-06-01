weight =float(input("Enter the patient's weight in kilograms:"))
def calculate_dosage(weight):
    dosage = weight * 0.1
    return dosage
result = calculate_dosage(weight)
print("The Calculated dosage is:", result)