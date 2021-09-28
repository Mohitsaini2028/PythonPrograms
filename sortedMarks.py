#Write a program to enter marks of 6 students and display them in sorted order.

marks = []
while(len(marks)<6):
    marks.append(int(input("Enter marks of Student "+str((len(marks)+1))+" ")))
    
print(sorted(marks))
