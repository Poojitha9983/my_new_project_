l1=[1,2,3,3,4,5,6,4,2]
dup=[]
for i in l1:
    if i not in dup:
        dup.append(i)
print(dup)