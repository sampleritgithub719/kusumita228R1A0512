a=[1,2,3,4,5]
b=[2,5,7,3,9]
c=[]
for i in a:
    if i in b:
        c.append(i)
        print(c)