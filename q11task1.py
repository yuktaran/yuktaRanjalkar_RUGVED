n=input("enter text for calculating grade level")
l=0
w=0
s=0
g=0
for letter in n:
    if letter.isalpha():
        l=l+1
for letter in n:
    if letter.isspace():
        w=w+1
for letter in n:
    if letter=="." or letter=="!" or letter=="?":
        s=s+1
l=(l/w)*100
w=(w/s)*100
g=0.0588*l-0.296*s-15.8
print(g)
