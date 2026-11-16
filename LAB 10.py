'''
#ans1
a=list(map(int,input().split()))
v=int(input())
t=tuple(a)
print("Tuple:",t)
print("Length:",len(t))
print("Count of",v,":",t.count(v))
print("First index of",v,":",t.index(v))
'''
'''
#ans2
def count_vowels(s):
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c+=1
    return c
t=input()
print("Vowels:",count_vowels(t))
'''
'''
#ans3
v=input().split()
c={}
o=[]
for n in v:
    if n in c:
        c[n]+=1
    else:
        c[n]=1
        o.append(n)
for n in o:
    print(n,":",c[n])
w=o[0]
for n in o:
    if c[n]>c[w]:
        w=n
print("Winner:",w)
'''
'''
#ans4
w=input()
f={}
for i in w:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
'''
'''
#ans5
def simple_interest(p,r,t=1):
    return p*r*t/100
p=float(input())
r=float(input())
print("1 year:",simple_interest(p,r))
print("3 years:",simple_interest(p,r,3))
'''
'''
#ans6
def get_grade(m):
    if m>=80:
        return 'A'
    elif m>=60:
        return 'B'
    elif m>=40:
        return 'C'
    else:
        return 'F'
n=int(input())
gc={}
o=[]
for i in range(n):
    l=input().split()
    name=l[0]
    m=int(l[1])
    g=get_grade(m)
    print(name,":",g)
    if g in gc:
        gc[g]+=1
    else:
        gc[g]=1
        o.append(g)
print("Grade count:")
r={}
for g in o:
    r[g]=gc[g]
print(r)
'''
'''
#ans7
a=tuple(map(int,input().split()))
e=()
for x in a:
    if x%2==0:
        e=e+(x,)
print(e)
'''
'''
#ans8
n=int(input())
d={}
for i in range(n):
    l=input().split()
    a=l[0]
    b=l[1]
    d[a]=b
q=input()
if q in d:
    print(d[q])
else:
    print("Not found")
'''
'''
#ans9
n=int(input())
s={}
o=[]
for i in range(n):
    l=input().split()
    x=l[0]
    q=int(l[1])
    s[x]=q
    o.append(x)
m=int(input())
for i in range(m):
    l=input().split()
    act=l[0]
    x=l[1]
    q=int(l[2])
    if act=="SELL":
        if q>s[x]:
            print("Insufficient stock:",x)
        else:
            s[x]-=q
    elif act=="ADD":
        if x in s:
            s[x]+=q
        else:
            s[x]=q
            o.append(x)
for x in o:
    print(x,s[x])
'''
'''
#ans10
def stats(a):
    small=a[0]
    big=a[0]
    for x in a:
        if x<small:
            small=x
        if x>big:
            big=x
    avg=sum(a)/len(a)
    return (small,big,avg)
a=list(map(int,input().split()))
print(stats(a))
'''
