import math

def is_prime(n):
	n = int(n)
	is_prime = True
	if n % 2 != 0:
		for i in range (3, int(math.sqrt(n))+1, 2):
			if n % i == 0 and is_prime:
				is_prime = False
	else: 
		is_prime = False
	return is_prime

def generate_keypair(p, q):
	if not (is_prime(p) and is_prime(q)):
		raise ValueError('Both numbers must be prime.')
	elif p == q:
		raise ValueError('p and q cannot be equal')

generate_keypair(input('Enter a first prime: '), input('Enter a second prime: '))

 







