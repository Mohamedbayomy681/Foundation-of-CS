# Function to perform modular exponentiation: (base^exp) % mod
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Function to load private key from a file
def load_private_key():
    with open("private_key.txt", "r") as priv_file:
        return int(priv_file.read().strip())

# Function to load ciphertext from a file
def load_ciphertext():
    with open("ciphertext.txt", "r") as cipher_file:
        c1, *c2 = map(int, cipher_file.read().split())
    return c1, c2

# Function to decrypt a ciphertext using the private key
def decrypt(private_key, p, ciphertext):
    c1, c2 = ciphertext
    s = mod_exp(c1, private_key, p)
    s_inv = pow(s, -1, p)
    m = [(msg * s_inv) % p for msg in c2]
    
    if all(isinstance(i, int) for i in m):
        m = ''.join(chr(i) for i in m)
    return m

if __name__ == "__main__":
    # Load private key and ciphertext
    private_key = load_private_key()
    c1, c2 = load_ciphertext()

    # Generate prime p and g (we need the values used during encryption)
    p = int(input("Enter the prime p used during encryption: "))
    g = int(input("Enter the generator g used during encryption: "))

    # Decrypt the message
    decrypted_message = decrypt(private_key, p, (c1, c2))
    print(f"Decrypted Message: {decrypted_message}")
