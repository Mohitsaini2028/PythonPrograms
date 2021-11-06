#Print following pattern: 1 12 123 1234 12345 123456 1234567 12345678 123456789
n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
