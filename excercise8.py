# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for element in roll_number:
    if element not in sample_dict.values():
        roll_number.remove(element)
print(roll_number)