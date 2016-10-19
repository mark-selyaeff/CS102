student = {'name': 'John', 'age': 18, 'University': 'MIT'}
print(student['name'])
student['grades'] = [70, 67, 93]

for key in student:
    print(key, ' ', student[key])
    '''
    name John
    age 18
    grades [1,2,3,...]
    '''

keys = student.keys() # Keys output
key = list(keys)

values = student.values()
values = list(values)

items = student.items
items = list(items) # [('name', 'John'), ('age', 18)]

for key, value in student.items():
    print(key, ' ', values)

def my_hash(s):
    h = 0
    for ch in s:
        h = h + ord(ch)
    return h

h = my_hash('a')
# h = 97
index = h % 5
# index = 2


words_list = ['Alice', 'in', 'worderland', ...]
    for word in words_list:
        if words[word] += 1
    else:
        words[word] = 1
words = defaultdict(int) # При обращении к несуществующему элементу выводится 0
d = {key:value for key, value in a_list}
