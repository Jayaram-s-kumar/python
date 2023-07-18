

n = int(input("Enter range:"))

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum*=i
    return sum

if(n==1):
    print("1")
else:
    print("1",end=" ")
    for i in range(1,n+1):
        print((i**i)/factorial(i),end=" ")
