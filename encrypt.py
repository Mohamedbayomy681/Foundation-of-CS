import random

# Function to perform modular exponentiation: (base^exp) % mod
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Function to load public key from a file
def load_public_key():
    with open("public_key.txt", "r") as pub_file:
        p, g, h = map(int, pub_file.read().split())
    return p, g, h

# Function to encrypt a message m using the public key
def encrypt(public_key, m):
    p, g, h = public_key
    if isinstance(m, str):
        m = [ord(c) for c in m]
    
    k = random.randint(1, p - 2)
    c1 = mod_exp(g, k, p)
    c2 = [(msg * mod_exp(h, k, p)) % p for msg in m]
    return c1, c2

if __name__ == "__main__":
    # Load the public key
    public_key = load_public_key()

    message = input("Enter a message (integer or string): ")

    # Encrypt the message
    ciphertext = encrypt(public_key, message)
    print(f"Ciphertext: {ciphertext}")

    # Save ciphertext to a file
    with open("ciphertext.txt", "w") as cipher_file:
        cipher_file.write(f"{ciphertext[0]} {' '.join(map(str, ciphertext[1]))}")
