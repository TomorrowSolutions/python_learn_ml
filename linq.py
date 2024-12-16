
"""
Операции над списками(типа линк)
"""


#Трансформация списков(создает список)
list2 = [item for item in range(1,6)]
list2= [item ** 3 for item in range(1,6)]
list2= [item ** 3 for item in range(1,6) if item % 2 ==0]
colors=['Red', 'orange', 'Yellow', 'green', 'Blue']
list2=[item.upper() for item in colors]
print('list2=',list2)

#Выражение-генератор(тоже самое, что и выше, но не создает список)
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
for value in (x ** 2 for x in numbers if x % 2 ==0):
	print(value,end=' ')
square_nechet= (x ** 2 for x in numbers if x % 2 ==0)
print(square_nechet)#<genexpr> вместо списка

#Фильтрация

def is_nechet(x):
	"""Возвращает true, если аргумент будет нечетным"""
	return x % 2 != 0
print(list(filter(is_nechet,numbers)))

#Фильтрация лямбда-выражения
print(list(filter(lambda x: x % 2 != 0, numbers)))

#Изменение списка методом map

print(list(map(lambda x: x ** 2, numbers)))
#map+filter
comb=list(map(lambda x: x ** 2,\
	filter(lambda x: x % 2 !=0,numbers)))
print(comb)

#min и max для строк лучше делать с использованием lower()
print(min(colors,key=lambda s:s.lower()))#blue
print(max(colors,key=lambda s:s.lower()))#yellow

#zip сцепляет несколько списков и создает кортежи

names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0]

for name,gpa in zip(names,grade_point_averages):
	print(f'Name={name};GPA={gpa}')
