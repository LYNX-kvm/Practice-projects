from random import randint

value_low = input("Lowest value?: ")
value_high = input("Highest value?: ")

if value_low.isdigit() and value_high.isdigit():
    value_low = int(value_low)
    value_high = int(value_high)
    if value_low <= value_high:
        print(randint(value_low, value_high))
    else:
        print("Error, lowest value is greater than highest value")
else:
    print("Error, inputs are not numbers")