# Exercise 2: Merge two Python dictionaries into one

def Merge(dict1,dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3=Merge(dict1,dict2)
print(dict3)


