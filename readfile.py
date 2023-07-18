txt = "PROGRAMMING IN PYTHON"

file = open("code.txt","w")
file.write(txt)
file.close()

file = open("code.txt","r")

content = file.read()

print(content)