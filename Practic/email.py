f = open('emails.txt')
emails_lst = f.readlines()
print(emails_lst)
emails_stripped = []
for email in emails_lst:
	emails_stripped.append(email.strip())
print(emails_stripped)
print(','.join(emails_stripped))
f.close()

''' with open('emails.txt') as f: 
		emails_lst = f.readlines
	emails_stripped = [email.(strip() for email in emails_lst]
	filter(is_function, a_list) — профильтровать список по функции (она возвращает 0 или 1 ) '''