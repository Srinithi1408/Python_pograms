#ARBITERY ARGUMENT

def sam_func(*kids):
    print(kids[:3])
sam_func('divya','sri','tamil','keerthi','surander')

#KEYWORD ARGUMENT

def samp1(lname,fname):
    print(lname+'kumar')
samp1(lname='sri',fname='nithi')

#AA

def fam(*kids):
    print(kids[-1])
fam('sri','tamil','surander','keerthi','udhaya')

#KW ARGUMENT(key word arbiteary aegument)

def samp2(**kids):
    print(kids['lname'])
samp2(fname='surander',sname='srinithi',tname='Tamil',lname='keerthi',uname='udhaya')
