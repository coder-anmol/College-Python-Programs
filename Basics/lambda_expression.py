add = lambda a, b: a + b

check_leap_year = lambda y: f"{y} is not Leap Year" if y % 4 else f"{y} is leap Year"

if (__name__ == "__main__"):
    number1 = int(input("Enter num1: "))
    number2 = int(input("Enter num2: "))
    print(f"Sum of {number1} and {number2} is {add(number1,number2)}")
    print(check_leap_year(2023))
