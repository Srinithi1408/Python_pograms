def Bill():
    n=int(input("Enter the Number of Units consumed: "))
    if (n>=0 and n<100):
        print ("Mil")
    elif(n>=100 and n<501):
        print (r," Rupees")
    elif (n>=501 and n<1001):
        r=n*10
        print(r," Rupees")
    elif (n>=1001 and n<2000):
        r=n*15
        print (r," Rupees")
    elif (n>=2000 and n<5000):
        r=n*20
        print (r," Rupees")
    elif (n>=5000 and n<10000):
        r=n*25
        print (r," Rupees")
    elif (n>=10000 and n<20000):
        r=n*50
        print (r," Rupees")
    elif (n>=20000):
        r=n*75
        print (r," Rupees")
    C=input ("\nDo you want to continue.....\ny or N: ")
    if(C=='Y'):
        Bill()

Bill ()
