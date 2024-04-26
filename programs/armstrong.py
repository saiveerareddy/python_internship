def is_armstrong_number(n):

    num_str = str(n)

    num_digits = len(num_str)


    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)


    return sum_of_powers == n



number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
