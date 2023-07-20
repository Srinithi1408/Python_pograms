a=(1,2,3,4,5)
i=int(input('Type the value of i:'))
j=int(input('Type the value of j:'))
n=int(input('Type the value of n:'))
try:
    print(a[4])
    print(i/j)
    print(i/n)
except IndexError:
    print('index erroe happened')
    print('hello')
except IndexError:
    print('index erroe happened')
    print('hello')
except NameError:
    print('NameError happened')
    print('hello')
print(a)
