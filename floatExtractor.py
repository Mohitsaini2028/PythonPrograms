#Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str = 'Y-tatata-acropolis: 0.8475'


number = (float(str[str.find(":")+1:]))
print(number,type(number))
