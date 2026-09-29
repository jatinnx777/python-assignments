#Program to take input of a string from user and display its length,first character and last character
str=input("enter any string")
print("length of the string is:",len(str))
print("first character of string is:",str[0])
print("Last character of string is:",str[-1])


#Program to display a string in lowercase and uppercase
str=input("enter any string")
print(str.lower())
print(str.upper())


str=input("enter any string")
str1=str.strip()
words=str1.split()
print(str1)
print(len(words))


str=input("enter any string")
str1=input("enter any other string")
if(str1 in str):
    print("yes substring is present")
else:
    print("substring is not present")




str=input("enter any string")
new=input("new word which is to be added")
old=input("word which needs to be removed")
str1=str.replace(old,new)
print(str1)



str=input("enter any string")
print(str[::-1])



str=input("enter any string")
reversed=""
for i in str:
    reversed=i+reversed
print(reversed)


str=input("enter any string")
words=str.split()
reversed_words=words[::--1]
str1="".join(reversed_words)
print(str1)
