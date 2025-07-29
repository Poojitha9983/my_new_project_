l1=[1,2,3,3,4,5,6,4,2]
duplicate=[]
for i in l1:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
