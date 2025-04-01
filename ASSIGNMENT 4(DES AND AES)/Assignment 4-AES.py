from Crypto.Cipher import AES
key = b'C&F)H@McQf9TjWnZ'  
cipher = AES.new(key, AES.MODE_EAX)
data = "Hello World".encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)