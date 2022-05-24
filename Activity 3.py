#!/usr/bin/env python
# coding: utf-8

# In[1]:


terms = int(input("How many terms? "))

result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])


# In[2]:


my_list = [12, 65, 54, 39, 102, 339, 221,]

result = list(filter(lambda x: (x % 13 == 0), my_list))

print("Numbers divisible by 13 are",result)


# In[4]:


dec = int(input('Enter a value: '))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[5]:


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[8]:


def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[9]:


def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("The L.C.M. is", compute_lcm(num1, num2))


# In[2]:


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input('Enter a number: '))

print_factors(num)


# In[3]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[4]:


import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(deck)

print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])


# In[6]:


import calendar

yy = int(input('Enter the year: ')) 
mm = int(input('Enter the month: '))    

print(calendar.month(yy, mm))


# In[8]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input('Enter a number: '))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[10]:


def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = int(input('Enter a number: '))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))


# In[11]:


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input('Enter a number: '))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[12]:


def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

dec = int(input('Enter a number: '))

convertToBinary(dec)
print()


# In[13]:


def name():
    return "John","Armin"

print(name())

name_1, name_2 = name()
print(name_1, name_2)

