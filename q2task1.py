word="Hello world"
wordarr=[]
for letter in word:
    if letter.isalpha():
        wordarr.append(letter.lower())
wordarr.sort()
for letter in wordarr:
    if letter.isalpha():
        print(letter,end="")
    else:
        continue
count=0
i=0
print()
for letter in wordarr:
    if  i==len(wordarr)-1:
        count+=1
        print(letter + " occurrence " + str(count))
    elif wordarr[i]!=wordarr[i+1]:
        count+=1
        print(letter + " occurrence " + str(count))
        count=0
    else:
        count+=1
    i+=1

