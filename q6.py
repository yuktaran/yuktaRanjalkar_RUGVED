n1=input("enter first word")
n2=input("enter second word")
a1=[]
a2=[]
for letter in n1:
    a1.append(letter)
for letter in n2:
    a2.append(letter)

a1.sort()
a2.sort()
i=0
f=0
for letter in a1:
    if letter==a2[i]:
        i=i+1
    else:
        f=1
        print("not anagrams")
        break
if f!=1:
    print("anagrams")