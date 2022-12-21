# Convert two lists into a dictionary 
kys = ['Ten', 'Twenty', 'Thirty']
val = [10, 20, 30]
d={}

for i in kys:
    d[i]=val[kys.index(i)]

print(d)