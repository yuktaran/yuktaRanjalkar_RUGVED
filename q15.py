n=int(input("enter no. of rows and columns in square matrix "))
arr=[[0 for i in range(n)] for j in range(n)]
brr=[[0 for i in range(n)] for j in range(n)]
crr=[[0 for i in range(n)] for j in range(n)]
for i in range(0,n):
    for j in range(0,n):
        arr[i][j]=int(input("enter element"))

for i in range(0,n):
    for j in range(0,n):
        print(arr[i][j],end=" ")
    print()

for i in range(0,n):
    for j in range(0,n):
        brr[i][j]=arr[j][i]

for i in range(0,n):
    for j in range(0,n):
        crr[i][j]=brr[i][n-j-1]

for i in range(0,n):
    for j in range(0,n):
        print(crr[i][j],end=" ")
    print()

for i in range(0,int((n-1)/2)+1):
    for j in range(i,n-i):
        print(arr[i][j],end=" ")
    for k in range(i+1,n-i):
        print(arr[k][j],end=" ")
    for l in range(i+1,n-i):
        print(arr[j][n-l-1],end=" ")
    for m in range(i+1,n-1-i):
        print(arr[n-m-1][n-l-1],end=" ")