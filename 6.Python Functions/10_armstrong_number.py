def is_armstrong(number):
    total = 0

    for digit in str(number):
        total += int(digit) ** 3

    return total == number


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")