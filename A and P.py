def area():
    print('\n\tArea of SHAPES')
    def Square():
        a=int(input('Enter the value of a:'))
        c=a*a
        d=a+a
        print('The Area of the Square is:',c)
        print('The Perimeter of the Square is:',d)
    def Rectangle():
        a=int(input('Enter the value of a:'))
        b=int(input('Enter the value of b:'))
        c=a*b
        d=a+b
        print('The Area of the Square is:',c)
        print('The Perimeter of the Rectangle is:',d)
    def Triangle():
        a=int(input('Enter the value of a:'))
        b=int(input('Enter the value of b:'))
        c=(1/2)*a*b
        d=(1/2)+a+b
        print('The Area of the Square is:',c)
        print('The Perimeter of the Triangle is:',d)
    def Circle():
        a=int(input('Enter the value of a:'))
        c=3.14*a*a
        d=3.14+a+a
        print('The Area of the Square is:',c)
        print('The Perimeter of the Circle is:',d)
    print('\t\t\nAREA OF DIFFERENT SHAPES USING FUNCTION')
    print('\nTO FINDTHE AREA OF THE SHAPES')
    print('\n\t1.Square')
    print('\n\t2.Rectangle')
    print('\n\t3.Triangle')
    print('\n\t4.Circle')
    ch=int(input('\nENTER YOUR CHOISE:'))
    if(ch==1):
        Square()
    elif(ch==2):
        Rectangle()
    elif(ch==3):
        Triangle()
    elif(ch==4):
        Circle()
    s=str(input('\nDo you whant to countinue (Y/N):'))
    if(s=='Y'):
        area()
    else:
        s=='N'
        print('Thankyou')
area()
        
