a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
print(a)
print(b)

for i in a:
    if i in b and i not in c:
        c.append(i)
        print(c)
print("Final Answer is :",c)

d=set(a).intersection(b)

print(d)

s=set(a)&set(b)
print(s)

print(type(s))
