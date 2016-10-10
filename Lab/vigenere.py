def length_equal(s, keyword):  # Уравнивание длины строк
    if len(s) > len(keyword):
        modulo = len(s) % len(keyword)
        keyword = keyword * (len(s) // len(keyword))
        if modulo:
            keyword = keyword + keyword[:modulo]
    else:
        keyword = keyword[:len(s)]
    return keyword


def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'PYTHON'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''  # Обнуляем строку
    keyword = length_equal(plaintext, keyword)
    for i in range(len(plaintext)):
        if (ord(plaintext[i].upper()) + ord(keyword[i].upper()) - 65) <= 90:
            ciphertext += chr(ord(plaintext[i].upper()) + (ord(keyword[i].upper()) - 65))
        else:
            ciphertext += chr(ord(keyword[i].upper()) - 91 + ord(plaintext[i].upper()))
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'PYTHON'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    keyword = length_equal(ciphertext, keyword)
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i].upper()) - (ord(keyword[i].upper()) - 65)) >= 65:
            plaintext += chr(ord(ciphertext[i].upper()) - (ord(keyword[i].upper()) - 65))
        else:
            plaintext += chr(ord(ciphertext[i].upper()) - ord(keyword[i].upper()) + 91)
    return plaintext


a = input('Enter a plaintext: ')
keyword = input('Enter a key: ')
print(encrypt_vigenere(a, keyword))
