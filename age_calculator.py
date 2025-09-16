def calculate_age(dob):
    today = datetime.today()
    dob_date = datetime.strptime(dob, "%d-%m-%Y")
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age

if __name__ == "__main__":
    dob = input("Enter your Date of Birth (dd-mm-yyyy): ")
    print(f"Your age is {calculate_age(dob)} years")