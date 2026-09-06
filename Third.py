#Question-1 Create a variable name and store your name in it
# name=input("Write down your namr:-")
# print(f"Hello {name}")

#Question-2 Take two number and perform arithmatic operations
# a=int(input("What is your frist number:-"))
# b=int(input("What is your second number:-"))
# print(f"{a+b},{a-b},{a*b},{a/b},{a//b},{a%b}")

#Question Take a word and print any words in between it
# a="Python"
# print(a[0:5:2])

#Question-4 Check whether age is greater or equal to 18
# a=int(input("What is your age:-"))
# if a>=18:
#     print("True")
# else:
#     print("Flse")

#Question-5 Print 1,2,3,4,5 using for loop
# for i in range(1,6):
#     print(i)

#Question-6 Using a while loop print 10-1
# a=10
# while a!=0:
#     print(a)
#     a-=1

#Question-7 Find the sum of numbers from 1-10 using a loop
# a=0
# for i in range(1,11):
#     a=a+i
# print(a)    

#Question-8 Count how many charecters are present
# a="Electrical"
# count=0
# for i in a:
#         count+=1
# print(count)

#Question-9 Print all even numnbers from 1-20
# for i in range(1,21):
#   if  i%2==0:
#     print(i)

#Question-10 Print the string in reverse order
a="Python"
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
print(rev)    
