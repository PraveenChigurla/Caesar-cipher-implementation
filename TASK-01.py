
data = input("enter data : ")
n = int(input("enter shift value : ")) #No.of shifts
cipher = ""

for i in range(len(data)): #Traversing through the data
    if data[i].isalpha():  #if data element is an Alphabet
        if data[i].isupper():  #if it's UpperCase(A-Z) UNICODES are from 65-90
            cipher += chr(((ord(data[i]) - 65 + n) % 26) + 65)
        elif data[i].islower():  #if it's UpperCase(a-z) UNICODES are from 97-122
            cipher += chr(((ord(data[i]) - 97 + n) % 26) + 97)
    else:
        cipher += data[i]

print("Cipher: " + cipher)
