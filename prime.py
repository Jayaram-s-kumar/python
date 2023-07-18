def prime(num):
    if num<=1:
        return False
    else:
        flag = False
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break
                return False
    
    if not flag:
        return True
    

for i in range(0,101):
    if i == 2:
        print(i)
    else:
        if prime(i):
            print(i)
    

