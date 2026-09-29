def fact(num):
    if (num==0 or num==1):
        return 1
    else:    
        return num*fact(num-1)
num=int(input("enter any number:"))
print(fact(num))



def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
num=int(input("enter any number:"))
print(fib(num))
for i in range(num):
    print(fib(i),end=" , ")




li=[10,20,35,40,50,60]
l1=list(filter(lambda x:x%2==0 , li))
print(l1)
l2=list(map(lambda x:x*2 , li))
print(l2)
from functools import reduce
sum=reduce(lambda x,y:x+y, li)
print(sum)




def student(name,age):
    print("name = ",name)
    print("age = ",age)
student("Ajay",80)
student(age=90,name="akshit")
def stu(clas,roll_no=1):
    print("class =",clas)
    print("roll_no = ",roll_no)
stu(10)
stu(11,11)
def stud(*args,**kwargs):
    print("positional items:",args)
    print("keyword items:",kwargs)
stud("ajay","akshit","amit","anmol",status="Present")