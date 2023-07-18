num = int(input("Enter number:"))

length = len(str(num))
sum = 0

for i in range(length):
    sum+=int(str(num)[i])**length

if sum == num:
    print("Armstrong")
else:
    print("not armstrong")


