n=int(input("enter the number"))
if n==1:
    print("0")
elif n==2:
    print("0 1")
else:
    a = 0
    b = 1
    c=1
    print("0",end=" ")
    for i in range(3, n+1):
        a=b
        b=c
        c=a+b
        print(str(a),end=" ")