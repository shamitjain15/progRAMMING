# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:14:10 2026

@author: lab
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:03:05 2026

@author: lab
"""
1
"""x= int(input("daalo:"))
y= int(input("daalo:"))
n= int(input("daalo:"))
for i in range(x,y+1):
    if i%n!=0:
        print(i)"""
2
"""x= int(input("daalo:"))
product=1
digits= 0
while x>0:
    digits=x%10
    product= product*digits
    x=x//10
print(product)"""
3
"""x= int(input("daalo:"))
L=0
S=0
while True:
    amt= int(input())
    if amt==-999:
        break
    if amt>x:
        L=L+1
    else:
        S=S+1
print(L)
print(S)"""
4
"""N= int(input("daalo:"))
P= int(input("daalo:"))
result=1
i=1
while N>0 and P>0 and i<=P:
    result= result*N
    i=i+1
print(result)"""
5
"""x= int(input("daalo:"))
y= int(input("daalo:"))
first= x
rev=0
while x>0:
    digit= x%10
    rev= rev*10+digit
    x= x//10
if rev==y:
    print("haaa")
else:
    print("naaa naaa naaa goriyeee")"""
6
# x= int(input("daalo:"))
# power=1
# for i in range(x):
#     print(power, end=" ")
#     power= power*2
7
x= int(input("daalo:"))
sum=0
i=1
while i*i<=x:
    if x%i==0:
        if i!=x//i:
            sum= sum+x//i
    i=i+1
    sum = sum-x
    if sum== x:
        print("perfect no")
    else:
        print("not that one")
  
 