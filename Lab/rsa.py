import math

def is_prime(n):
	n = int(n)
	is_prime = True
	if n % 2 != 0 and n > 2:
		for i in range (3, int(math.sqrt(n))+1, 2):
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
	print(e, n)
	print(d, n)


generate_keypair(input('Enter a first prime: '), input('Enter a second prime: '))

 







