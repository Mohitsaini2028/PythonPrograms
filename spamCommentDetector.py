# A spam comment is defined as a text containing following 
# keywords:
# “buy now” , “make a lot of money”, “subscribe this”, “click this”. 
# Write a program to detect these spams (hint: use ‘in’).

spamKeywords = ['buy now', 'make a lot of money','subscribe this','click this'] 

comment = input("Enter your Comment: ")

for i in spamKeywords:
    if i in comment:
        print("This is Spam Comment ")
        break

