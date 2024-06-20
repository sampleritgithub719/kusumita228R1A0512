rows = int(input("Enter the number of rows: "))

# Pattern of numbers
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(rows - i + 1, end=' ')
    print()
