# bmi_calculator.py

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

if __name__ == "__main__":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi}")
    if bmi < 18.5:
        print("You are Underweight")
    elif 18.5 <= bmi < 24.9:
        print("You are Normal weight")
    elif 25 <= bmi < 29.9:
        print("You are Overweight")
    else:
        print("You are Obese")
