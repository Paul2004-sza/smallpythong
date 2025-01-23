def calculate_square(number):
    return number ** 2

if __name__ == "__main__":
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        results = [f"The square of {int(num)} is {calculate_square(int(num))}" for num in numbers]
        print("\n".join(results))
    except ValueError:
        print("Please enter only valid numbers!")

