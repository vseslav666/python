from functools import reduce


def division_by_five(a):
    a = a % 5
    return a


data = [1, 4, 5, 30, 99]
print(list(map(division_by_five, data)))


def int_to_str(a):
    a = str(a)
    return(a)


data = [3, 4, 90, -2]
print(list(map(int_to_str, data)))


print(list(filter(lambda x: type(x) != str, data)))

data = ['some', 'other', 'value']

print(len((reduce(lambda x, y: x + y, data))))
