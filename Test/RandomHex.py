import secrets

Number = 10
if type(int(Number)) == int:
    for i in range(int(Number)):
        print(i,secrets.token_hex(nbytes=125),sep=' ',end='\n')
else:
    print("Enter a valid number to generate random number")
