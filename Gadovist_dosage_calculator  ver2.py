def calculate_dosage(weight):
    dosage = weight * 0.1
    return dosage

def convert_to_kilograms(weight, unit):
    if unit == "lbs":
        return weight * 0.45359237
    elif unit == "grams":
        return weight * 0.001
    else:
        return weight
    
while True:
    try:
        while True:
            weight_unit = input("Enter the unit of weight (kg/lbs/grams): ")
            if weight_unit.lower() not in ["kg","lbs","grams"]:
                raise ValueError("Invalid unit. Please enter a valid unit in (kg/lbs/grams).")
            else:
                break

        weight_input = float(input("enter the patient's weight in {}: ".format(weight_unit)))
        weight = convert_to_kilograms(weight_input, weight_unit)

        if weight <= 0:
            raise ValueError("weight mus be a positive value.")
        else:
            break 
    except ValueError as error:
        print("Invalid input. Please enter a valid weight.")
        print(error)

result = calculate_dosage(weight)
print("The calculated dosage is:", result)
