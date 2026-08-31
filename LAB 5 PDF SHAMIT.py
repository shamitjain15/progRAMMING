1
"""x= int(input("enter:"))
y= int(input("enter:"))
n= int(input("enter:"))
for i in range(x,y+1):
    if i%n==0:
        print(i)"""
    
    
2
"""x= int(input("enter:"))
s = 0
while x>0:
    l= x%10
    x= x//10
    s"= s+l
print"(s)"""
3
""""n= int(input("enter:"))
d=0
nd=0
x= int(input("enter:"))
while x!=-999:
    if x % n ==0:
        d = d+1
    else:
        nd=nd+1
    x= int(input("enter:"))
print(d)
print(nd)"""

4
"""x=int(input("enter:"))
if x<0:
    print("galat")
else:
    f = 1
    i=1
while i<=x:
    f=f*i
    i= i+1
print(f)"""
5    
"""x= int(input("enter:"))
rev= 0
while x>0:
    a= x%10
    rev= rev*10+a
    x=x//10
    
print(rev)"""
6
"""x=int(input("enter:"))
a=1
b=1
i=1
while i<=x:
    print(a)
    c=a+b
    a=b 
    b=c
    """
7
"""x=int(input("enter:"))
i=2
prime=1
if x < 2:
    prime=0
else:
    while i*i<=x:
        if x%i==0:
            prime=0
        i=i+1
        
if prime==1:
    print("PRIME")
else:
    print("NOT PRIME")"""
8
"""s = input("Enter a sentence: ")

i = 0
c = 0
sm = 0
d = 0
sp = 0

while True:
    try:
        x = s[i]
    except:
        break

    if x >= 'A' and x <= 'Z':
        c = c + 1
    elif x >= 'a' and x <= 'z':
        sm = sm + 1
    elif x >= '0' and x <= '9':
        d = d + 1
    else:
        sp = sp + 1

    i = i + 1

print("Capital =", c)
print("Small =", sm)
print("Digits =", d)
print("Special =", sp)"""