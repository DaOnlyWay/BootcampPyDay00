import sys


def operations(list):
    if len(list) == 1:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n  python operations.py 10 3")
        return
    if len(list) > 3:
        print("InputError: too many arguments")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n  python operations.py 10 3")
        return
    num1 = list[1]
    num2 = list[2]
    if num1.isdigit() == 0 or num2.isdigit() == 0:
        print("InputError: Only numbers")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n  python operations.py 10 3")
        return
    total = int(num1) + int(num2)
    print("Sum:", total,)
    total = int(num1) - int(num2)
    print("Difference:", total,)
    total = int(num1) * int(num2)
    print("Product:", total,)
    if int(num2) != 0:
        total = int(num1) / int(num2)
        print("Quotient:", total)
        total = int(num1) % int(num2)
        print("Remainder:", total,)
    else:
        print("ERROR (div by zero)\nERROR (modulo by zero)")


operations(sys.argv)
