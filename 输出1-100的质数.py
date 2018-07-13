j=2
bIsPrint=True
for i in range(3,100,1):
    for j in range(2,i//2+1,1):
        if(i%j==0):
            bIsPrint=False
            break
    if(bIsPrint==True):
        print(" " + str(i) + " ")
    bIsPrint=True

#recursion version
def PrimeNumber(NumberIn:int,i:int):
    if(NumberIn//2+1>i):
        if(NumberIn%i==0):
            #print("Number: " + str(NumberIn) + " is not a prime number.")
            return
        else:
            return PrimeNumber(NumberIn,i+1)
    else:
        print("Number: " + str(NumberIn) + " is a prime number.")

for i in range(3,100,1):
    PrimeNumber(i,2)

