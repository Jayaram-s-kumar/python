def countevenodd(n):
    evencount = 0
    oddcount = 0
    for num in n:
        if(num % 2==0):
            evencount+=1
        else:
            oddcount+=1
    return evencount , oddcount

numbers = []
n = int(input("Enter the total numbers of elements:"))
for i in range(1,n+1):
    element = int(input("Enter element %d:" %(i)))
    numbers.append(element)

eventcount , oddcount = countevenodd(numbers)

print("even count is %d" %(eventcount))
print("odd count is %d" %(oddcount))





   