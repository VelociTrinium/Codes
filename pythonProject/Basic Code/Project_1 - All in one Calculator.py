print("""
What Function do you want to perform (Please put the corresponding number)
1 : Addition
2 : Subtraction
3 : Multiplication
4 : Division
5 : Modulus (to check divisibility)
6 : Floor Division (to rounded off value after division)
7 : Exponential Power
8 : Sum of all numbers till 0
9 : XYZ Number Calculator
10 : Random Number Generator
""")

to_perform = 0

try:
    to_perform = float(input("What would you like to perform => "))
except ValueError:
    print("""!Error! -> Please input a number and not letters.
    """)

if float(to_perform) == 1:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")

elif float(to_perform) == 2:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")

elif float(to_perform) == 3:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    result = number_1 * number_2
    print(f"{number_1} * {number_2} = {result}")

elif float(to_perform) == 4:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    result = number_1 / number_2
    print(f"{number_1} / {number_2} = {result}")

elif float(to_perform) == 5:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    if number_1 % number_2 == 0:
        print(f"{number_1} is divisible by {number_2}")
    else:
        print(f"{number_1} is not divisible by {number_2}")

elif float(to_perform) == 6:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter number 2 > "))
    result = number_1 // number_2
    print(f"{number_1} / {number_2} is roughly = {result}")

elif float(to_perform) == 7:
    number_1 = float(input("Enter number 1 > "))
    number_2 = float(input("Enter power of 1 > "))
    result = number_1 ** number_2
    print(f"{number_1} ^ {number_2} = {result}")

elif float(to_perform) == 8:
    number_1 = float(input("Enter a number > "))
    sum_num = 0
    while number_1 > 0:
        sum_num += number_1
        number_1 -= 1
    print(f"sum of number is > {sum_num}")

elif float(to_perform) == 9:
    x_value = int(input("Input X value: "))
    x_value += 1
    y_value = int(input("Input Y value: "))
    y_value += 1
    z_value = int(input("Input Z value 'put 0 if not required': "))
    z_value += 1
    num_time = 0
    for x in range(x_value):
        for y in range(y_value):
            for z in range(z_value):
                print(f"{x}, {y}, {z}")
                num_time += 1
    print(f"Different possible outcomes are {num_time}")

elif float(to_perform) == 10:
    import random
    random_no_1 = random.randint(1, 10)
    random_no_2 = random.randint(1, 100)
    random_no_3 = random.randint(1, 1000)
    print(f"Random numbers are {random_no_1}, {random_no_2}, {random_no_3}")

else:
    print("Please enter the number of the function you want to perform.")
