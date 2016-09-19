s = 'Some ordinary string'
pattern = 'r'
pos = 0
while pos != -1:
	pos = s.find(pattern, pos)
	if pos != -1:
		print(pos)
		pos += 1



		

