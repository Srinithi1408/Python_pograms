#this is the program for Exception
a=(1,2,3,4,5)
i=int(input('Type the value of i:'))
j=int(input('Type the value of j:'))
try:
    print(a[6])
except IndexError:
    print('index erroe happened')
    print('hello')
try:
    print(i/j)
except IndexError:
    print('index erroe happened')
    print('hello')
try:
    print(i/m)
except NameError:
    print('NameError happened')
    print('hello')
