data = input("Enter a number or press enter to quit")
sum = 0

while True:
    if (data == ""):
        break
    else:
        sum+=int(data)
        data = input("Enter a number or press enter to quit")

print("sum is ",sum)

