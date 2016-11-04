# titanic
def survived(tit_data):
	count = 0
	for record in tit_data:
		count += int(record['survived'])
	return (count, len(tit_data) - count)

# с генератором

def survived(tit_data):
	count = [record['survived'] for record in tit_data]
	return (count, len(tit_data) - count)


def survived_by_sex(tit_data):
	tit_data_sorted = sorted(tit_data, key = itemgetter('sex'))
	groups = groupby(tit_data_sorted, key = itemgetter('sex'))
	for sex, group in groups:
		group = list(group)
		print(sex, ' ', survived(group))


# Сортировка кортежей по отдельному ключу (координате)
points = [(1, 0.5), (2, 0.1)]
points.sort(key = get_y)
points.sort(key = itemgetter(1, 0))

def get_y(point):
	return point[1]

# sorted - копия
# sort - изменяется исходный объект

