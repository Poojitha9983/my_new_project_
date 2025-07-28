l1=[1,2,3,3,4,5,6,4,2]
dupli=[]
for i in l1:
    if i not in dupli:
        dupli.append(i)
print(dupli)
