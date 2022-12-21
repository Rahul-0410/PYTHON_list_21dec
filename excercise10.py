# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

no_duplicate=set(sample_list)
print("unique items",list(no_duplicate))

tup=tuple(no_duplicate)
print("Tuple",tup)
print("Min :",min(tup))
print("MAx :",max(tup))
