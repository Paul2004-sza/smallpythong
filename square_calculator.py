def calculate_square(number):
    return number ** 2

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {calculate_square(num)}")
