s=input("enter a string")
n=int(input("enter a number"))
if len(s)%n!= 0:
    print("string cannot be divided into "+ str(n) +"parts")
else:
    st=s[0:n]
    print(st)
    str=""
    i=0
    f=0
    for i in range(0,len(s)):
        if(i%n==0):
            str=""
            for letter2 in s[i:i+n]:
                str=str+letter2
            if(st!=str):
                print("string cannot be divided into same chains")
                f=1
                break
            i=i+n
            print(i)
    if f==0:
        i=1
        for i in range(0,int(len(s)/n)):
            print(str,end=", ")
