n=int(input("enter the number"))
l=2*n-2
v=[int(l/2)]
i=1
c=0
k=0
f=0
for j in range (1,n+1):
    c=0
    k=0
    f=0
    if i==1:
        for k in range (0, l+1):
            if c==int(l/2):
                print("*",end="")
            else:
                print(" ",end="")
            c=c+1
    else:
        for p in range (0, len(v)):
            v[c]=v[c]-1
            c=c+1
        v.append(v[c-1]+2)
        for t in range (0, l+1):
            f=0
            m=0
            for o in range (0,len(v)):
                if v[m]==k:
                    f=1
                    break
                m=m+1
            if f==1:
                print("*",end="")
            else:
                print(" ",end="")
            k=k+1
    i=i+1
    print()
j=0
i=1
t=0
p=0
for j in range (1,n+1):
    c=0
    k=0
    f=0
    if i==n:
        for k in range (0, l+1):
            if c==int(l/2):
                print("*",end="")
            else:
                print(" ",end="")
            c=c+1
    else:
        for t in range(0,l+1):
            f=0
            m=0
            for o in range(0, len(v)):
                if v[m] == k:
                    f = 1
                    break
                m = m + 1
            if f == 1:
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        for p in range (0, len(v)-1):
            v[c]=int((v[c]+v[c+1])/2)
            c=c+1
        v.pop(c)
    i = i + 1
    print()
