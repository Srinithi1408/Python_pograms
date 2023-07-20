#READ FILE

f1=open('sample.txt','r')
d2=f1.readline(2)
print(d2)
d2=f1.readlines()
print(d2)
data=f1.read(7)
print(data)


d1=f1.read(15)
print(d1)

