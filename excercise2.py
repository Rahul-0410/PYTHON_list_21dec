# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
list = [34, 54, 67, 89, 91, 43, 94]

print("list after removing index 4 number")
list1=list.pop(4)
print(list)
print("list after adding elemnet at index 2")
item=list.insert(2,11)
print(list)
print("list after adding eleemnt at last")
item1=list.append(11)
print(list)

