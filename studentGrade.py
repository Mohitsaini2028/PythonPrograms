# Write a program to calculate the grade of a student from his marks of 
# the following scheme: 
# 90-100: Excellent
# 80-90: A
# 70-80: B
# 60-70: C
# 50-60: D
# Less than 50 : Fail

print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Excellent")
elif avg>=81 and avg<91:
    print("A")
elif avg>=71 and avg<81:
    print("B")
elif avg>=61 and avg<71:
    print("C")
elif avg>=51 and avg<61:
    print("D")
elif avg<51:
    print("Fail")
else:
    print("Invalid Input!")
