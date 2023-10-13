times=int(input("次数："))
conditions=input("")

account=[]
for i in range(8*times):
    account.append(conditions)

for i in range(1,n+1):
    numbers=0
    for j in range(1,j+1):
        if account[(i-1)*8:i*8]==account[(j-1)*8:j*8]:
            numbers=numbers+1
            print(numbers)
        
