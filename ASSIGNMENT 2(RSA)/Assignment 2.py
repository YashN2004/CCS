import sympy
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

if not (sympy.isprime(p) and sympy.isprime(q)):
    print("Both numbers must be prime.")

n = p * q
z = (p - 1) * (q - 1)

e = 2
while sympy.gcd(e, z) != 1:
    e += 1

d = pow(e, -1, z)

print("Public Key (n, e):", (n, e))
print("Private Key (n, d):", (n, d))

m = int(input("Enter a message (as a number) to encrypt: "))
if m >= n:
    print("Message must be smaller than n.")
   

c = pow(m, e, n)
print("Encrypted Message (Ciphertext):", c)

dec_m = pow(c, d, n)
print("Decrypted Message:", dec_m)