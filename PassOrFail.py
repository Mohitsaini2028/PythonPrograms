# Write a program to find out whether a student is pass or fail, if it 
# requires total 40% and at least 33% in each subject to pass. Assume 
#3 subjects and take marks as an input from the user.

sub1 = int(input("Enter marks of subject 1 : "))
sub2 = int(input("Enter marks of subject 2 : "))
sub3 = int(input("Enter marks of subject 3 : "))

percentage = (sub1+sub2+sub3)/3

if percentage>40:
    if (sub1 and sub2 and sub3) > 33:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")
