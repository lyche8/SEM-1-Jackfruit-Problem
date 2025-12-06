def calculate_bmi(weight_kg, height_cm, sex):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    sex = sex.lower()

    if sex == "male":
        if bmi < 20:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    elif sex == "female":
        if bmi < 19:
            category = "Underweight"
        elif bmi < 24:
            category = "Normal weight"
        elif bmi < 29:
            category = "Overweight"
        else:
            category = "Obese"

    else:
        category = "Invalid sex entered"

    return bmi, category


# Example usage
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
sex = input("Enter sex (male/female): ")

bmi, category = calculate_bmi(weight, height, sex)
print(f"BMI: {bmi:.2f}, Category: {category}")
