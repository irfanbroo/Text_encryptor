import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)
##print(f"chars: {chars}")
##print(f"key: {key}")

##ENCRYPTION
original_text = input("Enter the message you want to encrypt: ")
cipher_text = ""
for letters in original_text:
    idx = chars.index(letters)
    cipher_text += key[idx]
print(f"Original message: {original_text}")
print(f"Encrypted message: {cipher_text}")


##ENCRYPTION
cypher = input("Enter the encrypted message: ")
original = ""
for letters in cypher:
    idx = key.index(letters)
    original += chars[idx]
print(f"original message: {original}")