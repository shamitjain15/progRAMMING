# 1
# s = input("Enter a string: ")
# rev = " "
# for i in s:
#     rev= i+rev
# print(rev)
2
# s = input("Enter a sentence: ")
# count=0
# for i in s:
#     if i!=" ":
#         count=count+1
#     else:
#         count=0
# print(count)
3
# s = input("Enter a sentence: ")
# word = input("Enter the word: ")
# count=s.count(word)
# if count>=1:
#     print("yes")
# else:
#     print("no")
# print(count)
#next wala
# baadme
4
# # s = input("Enter a sentence: ")
# # a = "abcdefghijklmnopqrstuvwxyz"
# # count = 0
# # for i in a:
# #     if i in s.lower():
# #         count=count+1
   
# # if count==26:
# #     print("yes")
# # else:
#      print("no")

7
# s = input("Enter a string: ")
# rev = ""
# for i in s:
#     rev= i+rev
# if s==rev:
#     print("YES")
# else:
#     print("no")

5
# 5
# s = input("Enter a string: ")
# e= int(input("shift:"))
# total=" "
# a="abcdefghijklmnopqrstuvwxyz"
# for i in s:
#     z = a.index(i)
#     total= total+ a[(z+e)%26]
# print(total)
    
81
# x= [12,2,33,34,78]
# total=0
# for i in x:
#     total=total+i
    
# print(total)

82
# x= [12,2,33,34,78]
# product=1
# for i in x:
#     product=product*i

83
# x= [12,2,33,34,78]
# small=x[0]
# for i in x:
#     if i<small:
#         small=i
# print(small)
32
# '''s = input("Enter a sentence: ")
# word = input("Enter a word: ")
# count = 0
# i = 0
# while i <= len(s) - len(word):
#     j = 0
#     while j < len(word) and s[i + j] == word[j]:
#         j = j + 1
#     if j == len(word):
#         count = count + 1
#         i = i + len(word)
#     else:
#         i = i + 1
# if count > 0:
#     print("Word found")
# else:
#     print("Word not found")
# print("Occurrences:", count)'''
    
11
"""s = input("Enter paragraph ")
digits = 0
alphabets = 0
upper = 0
lower = 0
special = 0
for ch in s:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        alphabets = alphabets + 1
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    else:
        if ch != " ":
            special = special + 1
print("Digits:", digits)
print("Alphabets:", alphabets)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Special characters:", special)"""

12

'''s = input("Enter sentence ")
result = ""
for ch in s:
    found = False
    for x in result:
        if x == ch:
            found = True
    if not found:
        result = result + ch
print(result)'''


9

# a=[4,2,8,1,5]
# for i in range(5):
#     for j in range(4):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
6
# n=int(input())
# a=0
# b=0
# c=0
# d=0
# e=0
# while n!=-1:
#     n=int(input())
#     if n==1 or n==2:
#         a+=1
#     elif n==3 or n==4:
#         b+=1
#     elif n==5 or n==6:
#         c+=1
#     elif n==7 or n==8:
#         d+=1
#     elif n==9 or n==10:
#         e+=1
# t=a+b+c+d+e
# print(f"1-2: {#*a} {(a/t)*100:.2f}")
# print(f"3-4: {#*b} {(b/t)*100:.2f}")
# print(f"5-6: {#*c} {(c/t)*100:.2f}")
# print(f"7-8: {#*d} {(d/t)*100:.2f}")
# print(f"9-10: {#*e} {(e/t)*100:.2f}")  
10
'''s = input("Enter hyphen-separated words: ")
words = s.split("-")
for i in range(len(words)):
    for j in range(0, len(words) - i - 1):
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp
result = ""
for i in range(len(words)):
    if i > 0:
        result = result + "-"
    result = result + words[i]
print(result
