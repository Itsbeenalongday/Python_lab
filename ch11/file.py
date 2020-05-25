file = open('test.txt','w')
file.write('hello world')
file.close()

file = open('test.txt','r')
s = file.read()
print(s)
file.close()

with open('test.txt','r') as file:
    s = file.read()
    print(s)