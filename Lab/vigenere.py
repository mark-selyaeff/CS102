def length_equal(s, keyword): 
	if len(s) > len(keyword):
		modulo = len(s) % len(keyword)
		keyword = keyword * int((len(s) / len(keyword)))
		if modulo:
			keyword = keyword + keyword[:modulo]
	else:
		keyword = keyword[:len(s)]
	return keyword

def encrypt_vigenere(plaintext, keyword):
	ciphertext = '' # Обнуляем строку
	keyword = length_equal(plaintext, keyword)
	# Подгонка ключа под размер входного слова
	# if len(plaintext) > len(keyword):
	# 	modulo = len(plaintext) % len(keyword)
	# 	keyword = keyword * int((len(plaintext) / len(keyword)))
	# 	if modulo:
	# 		keyword = keyword + keyword[:modulo]
	# else:
	# 	keyword = keyword[:len(plaintext)]

	# Получаем зашифрованное слово	
	for i in range(len(plaintext)):
		if (ord(plaintext[i].upper()) + ord(keyword[i].upper()) - 65) <= 90:
			ciphertext += chr(ord(plaintext[i].upper()) + (ord(keyword[i].upper()) - 65))
		else:
			ciphertext +=  chr(ord(keyword[i].upper()) - 91 + ord(plaintext[i].upper()))
	return ciphertext

plaintext = input('Enter a plaintext: ')
keyword = input('Enter a key: ')
print(encrypt_vigenere(plaintext, keyword))


