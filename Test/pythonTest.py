import re
A='adbjhsabdshj.vjdb!@#$%$'
B = re.sub('[^A-Za-z0-9]+', '', A)
print(A,end='\n')
print(B,end='\n')

