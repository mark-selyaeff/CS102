# Шифровка
def encrypt_caesar(plaintext):
    plaintext = str(plaintext)
    ciphertext = ""
    for i in range(len(plaintext)):
        if (88 <= ord(plaintext[i]) <= 90) or (120 <= ord(plaintext[i]) <= 122):
            ciphertext += chr(ord(plaintext[i]) - 23)
        else:
            ciphertext += chr(ord(plaintext[i]) + 3)
    return ciphertext


# Расшифровка
def decrypt_caesar(ciphertext):
    ciphertext = str(ciphertext)
    plaintext = ""
    for i in range(len(ciphertext)):
        if (65 <= ord(ciphertext[i]) <= 67) or (97 <= ord(ciphertext[i]) <= 99):
            plaintext += chr(ord(ciphertext[i]) + 23)
        else:
            plaintext += chr(ord(ciphertext[i]) - 3)
    return plaintext


print(encrypt_caesar(input('Enter a word:')))
