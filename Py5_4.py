#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:26:53 2017

@author: foolwolf0068
"""

# 5.16
n1,n2=eval(input("Enter two number separated by coma:"))
if n1>n2:
    d=n2
    m=n1
else:
    d=n1
    m=n2

while True:
    if n1%d==0 and n2%d==0:
        print("The largest common factor is",d)
        break
    else:
        d-=1

while True:
    if m%n1==0 and m%n2==0:
        print("The smalleat multiply number is",m)
        break
    else:
        m+=1

# 5.20A
for i in range(1,8):
    for j in range(1,i):
        print(j,end=" ")
    print()
# 5.20B
for i in range(7,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
# 5.20C
for i in range(1,7):
    print(" "*2*(6-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# 5.20d
for i in range(6,0,-1):
    print(" "*2*(6-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 5.21
#n11=eval(input("Enter an non-negative int number:"))
for i in range(1,7):
    print(" "*2*(6-i),end="")
    for j in range(1,2*i-1):
        print(2**(j-1),end=" ")
        
    print(" "*2*(6-i),end="")
    print()
# 5.25
sum1=0
for i in range(1,50001):
    sum1+=1/i
print(sum1)
sum2=0
for i in range(50000,0,-1):
    sum2+=1/i
print(sum2)  

#5.26
sum3=0
for i in range(1,100,2):
     sum3+=i/(i+2)
print(sum3)

# 5.27

for n in range(10000,100001,10000):
    sum5=0
    for i in range(1,n+1):
        sum5+=((-1)**(i+1))/(2*i-1)
    print("n=",n,"PI is",4*sum5)

# 5.28
def factorial(n=2):
    if n<0:
        print("Please check your input",n)
        return 1
    elif n<=1:
        return 1
    else:
        return 1/(n*factorial(n-1))
for i in range(10000,100001,10000):
    sum6=0
    for j in range(1,i):
        sum6+=1/factorial(j)
    print("i=",i,"natural log e=",sum6)

# 5.35
n=1 #eval(input("Enter a number:"))
while n<10000:    
    sum2=0
    for i in range(n-1,0,-1):
        if n%i==0 :
            sum2+=i
    if sum2==n:
        print(n,"is a complete number.")
    n+=1
    
# 5.37
sum1=0
for i in range(1,625):
    sum1+=1/(i**0.5+(i+1)**0.5)
print(sum1)

