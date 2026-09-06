# a='hello how are you'
# print(a[6:9])
# print(a[:5])
# print(a[14:])

#Question-1
# age=input("what is your age:-")
# print("My age is",age)

#Question-2
# Myname = input("What is your name ? ")
# Age = input("What is your age ? ")
# Location = input("Where do you live ? ")
# print("My name is",Myname)
# print("I am ",Age, "years old")
# print("I live in ",Location)
# print("My name is",Myname,",","I am ",Age,"years old",",","I live in",Location,"." )
# print(f"My name is {Myname} , I am {Age} years old and I live in {Location}." )

#Question-3
# age= int(input("What is your age :-"))
# if age >= 18:
#     print("Elligible for vote")
# else:
#     print("Not Elligible")

#Question-4
# num1=int(input("What is your first number :-"))
# num2=int(input("What is your second number :-"))
# if num1>num2:
#     print(num1)
# elif num2>num1:
#     print(num2)
# else:
#     print("Both the numbers are equal")

#Question-5
# Gen=input("Write down your gender:-")
# if Gen in["Male","male","M","m"]:
#     print("Good morning sir")
# elif Gen in["Female","female","F","f"]:
#     print("Good mornig maam")
# else:
#     print("Others")

#Question-6
# num=int(input("Tell me your number:-"))
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd number")

#Question-7
# name=input("Write down your name :-")
# age=int(input("Write down your age:-"))
# if age>=18:
#     print(f"Heyy {name} you are a valid voter")
# else:
#     print(f"Hello {name} you can vote after {18-age} years" )

#Question-8
# year=int(input("Which year it is :-"))
# if year%400==0:
#      print(f"{year} is a century leap year") 
# elif year%100==0:
#      print(f"{year} is a common century year") 
# elif year%4==0:
#     print(f"{year} is a leap year ")
# else:
#     print("It is a common year")   

#Question-9
# temp=int(input("Please tell the temparature:-"))
# if temp>=-5 and temp<=5:
#     print("very cold")
# elif temp>=6 and temp<=18:
#     print("Cold")
# elif temp >=19 and temp<=30:
#     print ("Hot")
# elif temp<-5:
#     print("Extreme cold")
# else:
#     print("Extreme hot")

#For loop
# name="Arkapal"
# for i in range(1,11,1):
#     print(name)
#     print(i**3)
# n=int(input("Please tell your number:-"))
# # for i in range(n,n*10+1,n):
# for i   in range(1,11,1):
#     print(i**2)

#Question-10 Print Hello World n times
# num=int(input("What is your number:-"))
# for i in range (num):
#     print("Hello world")

#Question-11 Print natural numbers from 1 to n
# n=int(input("What is your number:-"))
# for i in range(1,n+1):
#     print(i)

#Question-12 Reverse for loop print n down to 1
# n=int(input("What is your number:-"))
# for i in range(n,0,-1):
#     print(i)

#Question-13 Print the multipication table of a number
# n=int(input("What is your number:"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

#Question-14 Sum of first n natural numbers
# s=0
# n=int(input("Till where  you want your sum:-"))
# for i in range(1,n+1):
#     s=s+i
# print(s)

#Question-15 Factorial of a number
# s=1
# n=int(input("What is your number:-"))
# for i in range(1,n+1):
#     s=s*i
# print(s)

#Question-16 Print the sum of all even number and odd number in a range separately
# n=int(input("What is your number:-"))
# oddsum=0
# evensum=0
# for i in range(1,n+1):
#     if i%2==0:
#         evensum=evensum+i
#     else:
#         oddsum=oddsum+i
# print(f"Your evensum is {evensum} and your oddsum is {oddsum}")

#Question-17 Print all factors of a number
# n=int(input("Please tell your number:-"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#Question-18 Check if a number is perfect(sum of factor = the number itsely)
# n=int(input("What is your number:-"))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s=s+i
# if s==n:
#     print("Perfect number")
# else:
#     print("Not perfect")

#Question-19 Check is a number is prime
# n=int(input("What is your number:-"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("Prime number")
# else:
#     print("Composite number")

#Question-20 Reverse a string without built-in function
# a="ARKAPAL"
# a=input("What is your word:-")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# if a==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

#Question-21 Count letters, digiits and special symbol in a string
# a=input("Write down your word:-")
# alpha=0
# digits=0
# spchar=0
# for i in a:
#     if i.isdigit():
#         digits+=1
#     elif i.isalpha():
#         alpha+=1
#     else:
#         spchar+=1
# print(f"Alphabets - {alpha},Digits - {digits},Special charecter - {spchar}")

#Question-22 Count letters, digiits and special symbol in a string without built-in function
# a=input("Write down your word:-")
# alpha=0
# digits=0
# spchar=0
# for i in a:
#     if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         digits+=1
#     elif ord(i)>=48 and ord(i)<=57:
#         alpha+=1
#     else:
#         spchar+=1
# print(f"Alphabets - {alpha},Digits - {digits},Special charecter - {spchar}")

#Question-23 Seperate each digit of a number and print a new line
# a=int(input("What is your number:-"))
# while a>=1:
#     print (a%10)
#     a=a//10

# a=int(input("What is your number:-"))
# rev=0
# while a>0:
#      rev=rev*10+a%10
#      a=a//10
# print(rev)

#Question-24 Check if the number is pallindrome
# a=int(input("What is your number:-"))
# copy=a
# rev=0
# while a>0:
#       rev=rev*10+a%10
#       a=a//10
# if rev==copy:      
#      print("Pallindrome")
# else:
#       print("Not pallindrome")  

#Question-25 Build a number guessing game - computer picks a random number, user keeps guessing untill correct
# import random 
# com=random.randint(1,100)
# tries=0
# while True:
#      tries+=1
#      hum=int(input("Please tell your number in between 1-100:-"))
#      if hum==com:
#           print(f"Congratulations you have won in {tries} tries")
#           break
#      elif hum>com:
#           print("Opps! try a little bit lower value")
#      elif hum<com:
#           print("Opps! try a little bit higher value")

#Question-26 Build a rock,paper,sizer game
# import random

# choices = ["rock", "paper", "scissors"]

# user = input("Enter rock, paper, or scissors: ").lower()

# computer = random.choice(choices)

# print("Computer chose:", computer)

# if user == computer:
#     print("It's a tie!")

# elif (user == "rock" and computer == "scissors") or \
#      (user == "paper" and computer == "rock") or \
#      (user == "scissors" and computer == "paper"):
#     print("You win!")

# else:
#     print("Computer wins!")

# Finding the number is pallindrome or not by using function approach     
# def pallindrome_checker(a):
#     copy=a
#     rev=0
#     while a>0:
#         rev=rev*10+a%10
#         a=a//10
#     if rev==copy:      
#         print("Pallindrome")
#     else:
#         print("Not pallindrome")  
# pallindrome_checker(121)
# pallindrome_checker(131)
# pallindrome_checker(165)
# pallindrome_checker(146)
# pallindrome_checker(111)

#Question-27 Print all the positive & negative elements separately
# lst=[3,-1,4,-5,9]
# pos=[]
# neg=[]
# for i in lst:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"your positive elements are {pos} and negative elements are {neg}" )        

#Question-28 Find the mean of all list elements
# lst=[10,20,30,40]
# sum=0
# for i in lst:
#     sum+=i
# print(sum/len(lst))    

#Question-29 Find the greatest element and print its index
lst=[4,8,2,9,1]
largest=lst[0]
index=0
for i in range(len(lst)):
    if lst[i]>largest:
        largest=lst[i]
        index=i
print(f"Your largest value is {largest} at index {index}")        

