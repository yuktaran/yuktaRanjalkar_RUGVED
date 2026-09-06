#A hill number is a number that has the same digit in the first & the last, but that's not all.
# In a hill number the first digits are strictly increasing until the largest digit,
# and after the largest digit, the last digits are strictly decreasing.
# The largest digit can be repeated but consecutively only, meaning no gaps by smaller numbers.

num=input("Enter a number: ")
l=len(num)
if num[0]!=num[l-1]:
    print(num+ " is not a hill number")
else:
    large=0
    i=0
    for letter in num:
        if int(letter)>int(num[large]):
            large=i
        i+=1
    i=0
    f=0
    for letter in num[0:large-1]:
        if int(num[i])> int(num[i+1]):
            print(num+ " is not a hill number")
            f=1
            break
        i+=1
    if f!=1:
        j=0
        for letter in num[0:l]:
            if int(letter)==int(num[i+1]):
                if int(num[j])!=int(num[j+1]):
                    break
            j+=1
        i=j
        print(j)
        for letter in num[j:l-2]:
            if int(num[i])< int(num[i+1]):
                print(num+" is not a hill number")
                f=1
                break
        if f!=1:
            print(num+ " is a hill number")

