# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]


counts ={}
for item in my_list:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] += 1

print(counts)