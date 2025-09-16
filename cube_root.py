
def cube_root(x):
    return round(x ** (1/3), 4)

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print(f"Cube root of {num} is {cube_root(num)}")