n=input("enter string to be encrypted")
s=int(input("enter shift key"))
enc=""
n=n.lower()
for letter in n:
    if letter.isalpha():
        if ord(letter) + s > 122:
            enc = enc + chr(122 - ord(letter) - s)
        else:
            enc = enc + chr(ord(letter) + s)
print(enc)