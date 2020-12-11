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
        for primes in primeList:
            print(primes, end=" ")
    else:
        num += 1
        checkPrime(num)

if(maxLimit > 0):
    checkPrime(num)
elif(maxLimit == 0):
    print([])
else:
    print("Please enter a positive numbers range!")







# num = int(input("Enter number "))
# p = 2
# while num != 0:
    # for i in range(2, p):
        # if p % i == 0:
            # break
    # else:
        # print(p, end=" ")
        # num -= 1
    # p += 1