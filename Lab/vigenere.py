def encrypt_vigenere(plaintext, keyword):
	ciphertext = ''
	if len(plaintext) > len(keyword):
		modulo = len(plaintext) % len(keyword)
		keyword = keyword * int((len(plaintext) / len(keyword)))
		if modulo:
			keyword = keyword + keyword[:modulo]
	else:
		keyword = keyword[:len(plaintext)]
	for i in range(len(plaintext)):
		ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 65)
	return ciphertext

plaintext = input('Enter a plaintext: ')
keyword = input('Enter a key: ')
print(encrypt_vigenere(plaintext, keyword))


