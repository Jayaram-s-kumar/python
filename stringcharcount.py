countdata = {}
string = input("Enter the string:")

sting_length = len(string)

for char in string:
    count = 0
    for i in range(sting_length):
        if (char == string[i]):
            count +=1
            #adding each character and its corresponding frequency to a dictionary.
            countdata[char] = count

    count = 0

for key,value in countdata.items():
    print(f" {key} : {value}\n")

