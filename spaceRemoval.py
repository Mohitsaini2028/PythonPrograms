# Write a Python program to remove spaces from a given string.
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("this i s a exam ple"))
print(remove_spaces("a b c"))
