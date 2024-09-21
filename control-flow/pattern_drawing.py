square_length = int(input("Enter the size of the pattern:"))
num_rows=0

while num_rows <square_length:
    num_columns = 0
    while num_columns<= square_length:
        num_columns += 1
        print("*", end="")
    print()
    num_rows +=1