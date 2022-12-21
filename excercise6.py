# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection=first_set&second_set
print("Intersection is",intersection)

final=first_set-intersection
print("First set after removing common elements")
print(final)

