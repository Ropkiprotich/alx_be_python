number=int(input("Enter a number to see its multiplication table:"))

for numbers in range(1,11):
    result = number * numbers
    print(f"{number} * {numbers} = {result}")
