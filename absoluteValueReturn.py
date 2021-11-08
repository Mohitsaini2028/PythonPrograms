#First, def a function called calculate_distance, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "No value". Check if it works calling the function with 9.6 and "what?".

def calculate_distance(arg):
    if type(arg) is float  or type(arg) is int:
        return abs(arg) #returning absolute value
    else:
        return "No Value"

print(calculate_distance(9.5))
