from Crypto.Cipher import AES
from secrets import token_bytes 

key = token_bytes (16)  
cipher = AES.new(key, AES.MODE_EAX)


data = input("Enter the data to encrypt: ").encode()  

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data) 

print("Cipher text:", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("Plain text:", plaintext.decode()) 
