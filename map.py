from functools import reduce

data = [1, 4, 5, 30, 99]
print(list(map(lambda a: a % 5, data)))

data = [3, 4, 90, -2]
print(list(map(lambda a: str(a), data)))

data = ['some', 1, 'v', 40, '3a', str]
print(list(filter(lambda x: type(x) != str, data)))

data = ['some', 'other', 'value']
print(len((reduce(lambda x, y: x + y, data))))
