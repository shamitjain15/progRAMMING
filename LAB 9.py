'''
#ans1
a=list(map(int,input().split()))
e=[]
o=[]
for x in a:
    if x%2==0:
        e.append(x)
    else:
        o.append(x)
print("Even:",e)
print("Odd:",o)
'''
'''
#ans2
s=input()
w=s.split()
r=[]
for i in w:
    if len(i)>3:
        r.append(i)
print(r)
'''
'''
#ans3
b=input().split()
t=0
w=0
bd=0
ov=[]
c=0
n=0
for i in b:
    if i=='W':
        w+=1   # wicket, no runs
    else:
        r=int(i)
        t+=r
        c+=r
        if r==4 or r==6:
            bd+=1
    n+=1
    # over complete
    if n%6==0:
        ov.append(c)
        c=0
if n%6!=0:
    ov.append(c)
print("Total Runs:",t)
print("Wickets:",w)
print("Boundaries:",bd)
print("Runs per over:",ov)
'''
'''
#ans4
a=list(map(int,input().split()))
big=a[0]
small=a[0]
for x in a:
    if x>big:
        big=x
    if x<small:
        small=x
print("Largest:",big)
print("Smallest:",small)
'''
'''
#ans5
s=input()
w=s.split()
p=w[0]
for x in w:
    if len(x)>len(p):
        p=x
print(p)
'''
'''
#ans6
m=input().split()
p=list(map(int,input().split()))
o=input().split()
q={}
for i in o:
    if i in q:
        q[i]+=1
    else:
        q[i]=1
t=0
for i in range(len(m)):
    x=m[i]
    if x in q:
        c=q[x]*p[i]
        print(x,"x",q[x],"=",c)
        t+=c
print("Total:",t)
'''
'''
#ans7
s=input()
w=s.split()
r=[]
for i in w:
    r.append(i[::-1])
print(" ".join(r))
'''
'''
#ans8
s=input()
d=[]
for i in s:
    if i.isdigit():
        d.append(int(i))
print(d)
print("Sum:",sum(d))
'''
'''
#ans9
n=int(input())
d={}
for i in range(n):
    s=input().lower()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
    p=s.split()
    a=p[0]
    b=p[1]
    c=d[s]
    if c==1:
        e=a+"."+b+"@jklu.edu.in"
    else:
        e=a+"."+b+str(c)+"@jklu.edu.in"
    print(e)
'''
'''
#ans10
a=list(map(int,input().split()))
p=[]
q=[]
for x in a:
    if x==0:
        q.append(x)
    else:
        p.append(x)
print(p+q)
'''
