#Take input of age of 3 people by user and determine oldest and youngest among them.

age = []
i=0
while(i<3):
    age.append(int(input(f" Enter age of {i+1} person : ")))
    i+=1
    
max_age=max(age)
max_index=age.index(max_age)

min_age=min(age)
min_index=age.index(min_age)

print(f" {max_index+1} person is the Oldest and {min_index+1} person is the Youngest ")
