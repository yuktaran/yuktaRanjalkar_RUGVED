word=input("Enter a word")
word=word.lower()
wordarr=[]
for letter in word:
    if letter.isalpha():
        wordarr.append(letter)
i=0
j=0
pos=0
for letter1 in range(len(wordarr)-1):
    pos = i
    j = i+1
    for letter2 in range(i+1,len(wordarr)):
        if wordarr[pos]>wordarr[j]:
            pos=j
        j+=1
    wordarr[i],wordarr[pos]=wordarr[pos],wordarr[i]
    i+=1

for letter in wordarr:
    print(letter,end="")



