def rankcard():
    Name=str(input("Name:"))
    Class=str(input("Class:"))
    Number =int(input("Reg.num:"))
    Tamil=int(input('Enter your Tamil mark:'))
    English=int(input('Enter your English mark:'))
    Maths=int(input('Enter your Maths mark:'))
    Science=int(input('Enter your Science mark:'))
    Social=int(input('Enter your Social mark:'))
    if(Tamil>=35 and English>=35 and Maths>=35 and Science>=35 and Social>=35):
            s="PASS"
            t="ALL THE BEST"
            avg=(Tamil+English+Maths+Science+Social)/5
            if(avg>=90):
                g=("Grade: O")
            elif(avg>=80):
                g=("Grade: A")
            elif(avg>=70):
                g=("Grade: B")
            elif(avg>=60):
                g=("Grade: C")
            elif(avg>=40):
                g=("Grade: D")
    else:
            s=("FAIL")
            g=('Grade: RA')
            t=("BETTER LUCK NEXT TIME")
    print('\t\t\t----------------------------------------------------------------')
    print('\t\t\t|\t\t\t\t\tMark Sheer\t\t|')
    print('\t\t\t|\t\t\t\tRanganathar collage\t\t|')
    print('\t\t\t|\t\t\t\t\tResult\t\t\t|')
    print('\t\t\t|\tName   :',Name,'\t\t\t\t\t\t|')
    print('\t\t\t|\tClass  :',Class,'\t\t\t\t\t|')
    print('\t\t\t|\tNumber :',Number,'\t\t\t\t\t\t|')
    print('\t\t\t|\tTamil  :',Tamil,'\t\t\t\t\t\t|')
    print('\t\t\t|\tEnglish:',English,'\t\t\t\t\t\t|')
    print('\t\t\t|\tMaths  :',Maths,'\t\t\t\t\t\t|')
    print('\t\t\t|\tScience:',Science,'\t\t\t\t\t\t|')
    print('\t\t\t|\tSocila :',Social,'\t\t\t\t\t\t|')
    print('\t\t\t----------------------------------------------------------------')
    print('\t\t\t|\tResult :',s,'\t\t',g,'\t\t\t|')
    print('\t\t\t|\t\t\t\t\t',t,'\t\t|')
    print('\t\t\t----------------------------------------------------------------')
    ch=input('Do you want to countinue (Y/N):')
    if (ch=='Y'):
        rankcard()
rankcard()
