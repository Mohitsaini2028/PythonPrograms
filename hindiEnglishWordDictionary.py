#• Write a program to create a dictionary of Hindi words with values as 
# their English Translation. Provide user with an option to look it up.

dictionary = {
        'जैसा':'as',
        'मैं':'I',
        'उसके':'his',
        'कि':'that',
        'वह':'he',
        'था':'was',
    }
print("These are the available word you can search any word to find it's meaning \n")
for key in dictionary:
    print(key,end=' ')

word = input("\n\nSearch any word : ")

if dictionary[word]:
    print(dictionary[word])
else :
    print("No such word exist")
