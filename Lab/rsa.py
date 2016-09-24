import math

def is_prime(n):
	n = int(n)
	is_prime = True
	for i in range (3, int(math.sqrt(n))):
		if n % i == 0 and is_prime:
			is_prime = False
	return is_prime
print(is_prime(input("Enter a number: ")))