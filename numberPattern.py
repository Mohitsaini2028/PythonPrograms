#Print following pattern: 1 22 333 4444 55555 666666 7777777 88888888 999999999

n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()
