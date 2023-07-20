a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))

#ARITHMATIC OPERATION
print("\n\t\tArithmatic Operations")
addition = lambda a,b:a+b
print("\n\tThe Addition value of",a,"and",b,"is:",addition(a,b))
subraction = lambda a,b:a-b
print("\n\tThe Subraction value of",a,"and",b,"is:",subraction(a,b))
multiplication = lambda a,b:a*b
print("\n\tThe multiplication value of",a,"and",b,"is:",multiplication(a,b))
division = lambda a,b:a/b
print("\n\tThe division value of",a,"and",b,"is:",division(a,b))

#BITWISE OPERATION
print("\n\t\tBitwise Operation")
bitwice_and=lambda a,b:a&b
print("\n\tThe Bitwise_AND value of",a,"and",b,"is:",bitwice_and(a,b))
bitwice_or=lambda a,b:a^b
print("\n\tThe Bitwise_OR value of",a,"and",b,"is:",bitwice_or(a,b))
bitwice_xor=lambda a,b:a|b
print("\n\tThe Bitwise_XOR value of",a,"and",b,"is:",bitwice_xor(a,b))
bitwice_not=lambda a,b:~a
print("\n\tThe Bitwise_NOT value of",a,"and",b,"is:",bitwice_not(a,b))
bitwice_rightshift= lambda a,b:a<<b
print("\n\tThe Bitwise_Right shift value of",a,"and",b,"is:",bitwice_rightshift(a,b))
bitwice_leftshift= lambda a,b:a>>b
print("\n\tThe Bitwise_Left shift value of",a,"and",b,"is:",bitwice_leftshift(a,b))

#LOGICAL OPERATION
print("\n\t\tLogic Operation")
logical_and=lambda a,b:(a>b) and (a<b)
print("\n\tThe Logical_And value of",a,"and",b,"is:",logical_and(a,b))
logical_or=lambda a,b:(a>b) or (a<b)
print("\n\tThe Logical_Or value of",a,"and",b,"is:",logical_or(a,b))
logical_not=lambda a,b:not (a>b)
print("\n\tThe Logical_Not value of",a,"is:",logical_not(a,b))
