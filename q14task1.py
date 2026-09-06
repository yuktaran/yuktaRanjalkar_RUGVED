arr=[]
num=int(input("enter the number"))
for i in range(0,num):
    arr.append(i)
i=0
f=0
for i in range(0,num):
    for j in range(i+1,num):
        if arr[i]==arr[j]:
            f=1
            break
    if f==1:
        break

if f==0:
    print("no repeating elements")
else:
    print(str(arr[i])+" is repeated at " + str(i)+ " and "+ str(j))
