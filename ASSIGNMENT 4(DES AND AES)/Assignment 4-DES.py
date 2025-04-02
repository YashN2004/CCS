from Crypto.Cipher import DES
from secrets import token_bytes 
 

key = token_bytes(8)  
cipher = DES.new(key, DES.MODE_EAX)

data = input("Enter the data to encrypt: ").encode()  

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data) 

print("Cipher text:", ciphertext)

cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("Plain text:", plaintext.decode())
