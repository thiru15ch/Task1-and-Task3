maxLimit = int(input("Enter your value: "))
primeList = []
num = 2
def checkPrime(num):
    count = 0
    for y in range(1, num+1):
        if((num%y) == 0):
            count += 1
    if(count == 2):
        primeList.append(num)
    if(len(primeList) == maxLimit):
        print(*primeList, sep=",")
    else:
        num += 1
        checkPrime(num)

if(maxLimit > 0):
    checkPrime(num)
elif(maxLimit == 0):
    print([])
else:
    print("Please enter a positive numbers range!")




