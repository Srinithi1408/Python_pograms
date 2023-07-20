#WRITE A PYTHON SCRIPT TO CALCULATE THE AREA OF TRIANGLE AND IMPLEMENT AL LEAST 3 EXCEPTION.
#USING ELSE AMD FINALLY CLAUSE

a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
try:
    k=(1/2)*a*b
    print('Area of the Triangle :',k)
except ZeroDivisionError :
    print('Zero Division Error happend:')
except NameError:
    print('Name Error Happend')
except ValueError:
    print('Value Error Happend')
finally:
    print('Area of Triangle Calculation is Over')
