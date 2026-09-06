def pattern(n):
    v1=[0]
    v2=[2*n-2]
    i=0
    f=0
    for j in range(0,2*n-1):
        f=0
        q=0
        if i<n:
            if i==0:
                for p in range(0,2*n-1):
                    if q==0 or q==2*n-2:
                        print("*",end="")
                    else:
                        print(" ", end="")
                    q=q+1
            else:
                v1.append(v1[len(v1)-1]+1)
                q=0
                for p in range(0,len(v2)):
                    v2[q]=v2[q]-1
                    q=q+1
                v2.append(v2[q-1]+1)
                q=0
                m=0
                for p in range(0,2*n-1):
                    m=0
                    f=0
                    for t in range(0,len(v1)):
                        if q==v1[m] or q==v2[m]:
                            f=1
                            break
                        m=m+1
                    if f==1:
                        print("*",end="")
                    else:
                        print(" ",end="")
                    q = q + 1
        else:
            if i==2*n:
                for p in range(0,2*n-1):
                    if q==0 or q==2*n-2:
                        print("*",end="")
                    else:
                        print(" ", end="")
                    q=q+1
            else:
                v1.pop()
                for p in range(0,len(v2)):
                    v2[q]=v2[q]+1
                    q=q+1
                v2.pop()
                q=0
                m=0
                for p in range(0,2*n-1):
                    m=0
                    f=0
                    for t in range(0,len(v1)):
                        if q==v1[m] or q==v2[m]:
                            f=1
                            break
                        m=m+1
                    if f==1:
                        print("*",end="")
                    else:
                        print(" ",end="")
                    q = q + 1
        i=i+1
        print()

num=int(input("enter the number"))
pattern(num)