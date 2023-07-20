#EXCEPTION WITH FINALLY

i=int(input('enter the value:'))
j=int(input('enter the value:'))
try:
    k=(i+j)/(i-j)
except ZeroDivisionError:
    print('Zero division happend')
else:
    print('your output is ready:',k)
finally:
    print("Exegution is over ❌❌❌❌💔")
