# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
lst=[]
for i in len(l1):
    if i%2==0:
        lst.append(l1[i])
    else:
        lst.append(l2[i])
print(lst)
