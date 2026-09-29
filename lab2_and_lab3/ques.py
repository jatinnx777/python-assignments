#Take two numbers as input from users and them
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
sum=num1+num2
print(sum)

#to check if a given number is positive , negatice or zero
num=int(input("enter any number"))
if(num>0):
    print("the given number is positive")
elif(num<0):
    print("the give number is negative")
else:
    print("the given number is zero")


#To find Largest of three numbers
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
if(num1>num2 and num1>num3):
    print(num1,"is largest")
elif(num2>num3 and num2>num1):
    print(num2,"is largest")
else:
    print(num3,"is largest")


#To display week days name from 1-7
num=int(input("enter any number"))
if (num==1):
    print("monady")
elif(num==2):
    print("tuesday")
elif(num==3):
    print("Wednesday")
elif(num==4):
    print("Thursday")
elif(num==5):
    print("Friday")
elif(num==6):
    print("Saturday")
elif(num==7):
    print("Sunday")
else:
    print("invalid input")


#Program to priitn multiplication table of a given number
num=int(input("enter any number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


num=int(input("enter any natural number"))
sum=0
i=1
while(i<=num):
    sum=sum+i
    i=i+1
print(sum)

#To check if a given number is prime or not
num=int(input("Enter a positive number:"))
isprime=True
if(num==1):
    print("number is neither prime nor composite")
else:
    for i in range(2,num):
        if num % i == 0:
            isprime=False
            break
        else:
            isprime=True
if(isprime):
    print("number is prime number")
else:
    print("number is not a prime number")


