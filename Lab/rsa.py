import math


def is_prime(n):
    n = int(n)
    is_prime = True
    if n % 2 != 0 and n > 2:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0 and is_prime:
                is_prime = False
    elif n <= 1 or n % 2 == 0:
        is_prime = False
    return is_prime


def gcd(a, b):
    a = int(a)
    b = int(b)
    return gcd(b, a % b) if b else a


def gcd_extended(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - y * (a // b)


def generate_keypair(p, q):
    p = int(p)
    q = int(q)
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q
    phi = (p-1)*(q-1)

    for i in range(3, phi, 2):
        if is_prime(i) and gcd(phi, i) == 1:
            e = i
            break
    x, y, d = gcd_extended(phi, e)
    d = d % phi
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
