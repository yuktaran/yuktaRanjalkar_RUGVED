#Start from the second-to-last digit and move left, doubling every alternate (second) digit.
# Subtract 9 from any doubled number that becomes 10 or higher (or add its two digits together).
# Add all the numbers you just got together with the untouched digits (the odd positions from the right).
# Check the total sum. If the total ends in 0 (meaning it can be divided by 10 with no remainder), the card number passes the test
c=input("enter credit card number")
v=[]
rev=""
for letter in c:
    rev=letter+rev
i=0
for letter in rev:
    if i%2!=0:
        n=int(rev[i])
        n=n*2
        if n>=10:
            n=n-9
        v.append(n)
    i=i+1
i=0
sum=0
for letter in rev:
    if i%2!=0:
        sum=sum+int(v[i])
    else:
        sum=sum+int(rev[i])
    i=i+1
if sum%10==0:
    print("valid number")
else:
    print("invalid number")


