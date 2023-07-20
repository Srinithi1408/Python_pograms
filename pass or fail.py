osubject1=int(input("Enter the First mark:"))
subject2=int(input("Enter the Second mark:"))
subject3=int(input("Enter the Third mark:"))
subject4=int(input("Enter the Fourth mark:"))
subject5=int(input("Enter the Fifth mark:"))
avg=(subject1+subject2+subject3+subject4+subject5)/5
if(avg>=90):
    print("This Student is pass in Distingtion")
if(avg>=80):
    print("Student pass in first class")
if(avg>=70):
    print("Student pass in Second class")
if(avg>=60):
    print("Student pass in Third class")
else:
    print("Want to work hard")


