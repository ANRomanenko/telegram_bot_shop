import sys

print(sys.version_info)

flag = True
if flag:
    print('Да')

print()

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i : i['y'])
print(points)

print()

# list_comprehension.py
listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)

print()

# powersum


def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённую в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))


stroka = "Это первое предложение. \
Это второе предложение"

print(stroka.replace('о', 'а'))
print(eval('2*3'))
print()
#

name = ['name', 'price', 'number']
spisok = []
number = 0

for i in name:
    spisok +=[i]
print(spisok[::-1])

spisok.append('add')
print(name)
print(spisok)