def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum*=i
    return sum

n = int(input("Enter the value of n:"))
print(factorial(n))