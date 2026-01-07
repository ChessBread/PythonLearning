import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()


random.shuffle(key)




#encrypt

plaintext = input("enter a messege to encrypt: ")
cipher_text = ""


for letter in plaintext:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plaintext}")
print(f"encrypted message : {cipher_text}")


#decrypt
cipher_text = input("enter a messege to encrypt: ")
plaintext = ""


for letter in cipher_text:
    index = key.index(letter)
    plaintext += chars[index]

print(f"encrypted message : {cipher_text}")
print(f"original message : {plaintext}")
