#WRITE FILE

f1=open('sample11.txt','w')
for i in range(0,7):
    name=input('name')
    f1.write(name)
    f1.write('\n')
f1.close()
