#spiski.py

"""
Операции со списками
"""

c = [-45, 6, 0,]+[ 72, 1543]

#for i in range(len(c)):
#	print(f'{i+1} {c[i]}')

a=[1,2,3]
b=[1,2,3]
d=[1,2,3,4]
f=[5,6,7]

print(a>=b)

#Присоединение кортежа к списку

a+=(5,6,7)
print(a)

#Удаление элемента из списка

del a[-1]
print(a)

def modify_elements(items):
	"""Умножение всех элементов на 2"""
	for i in range(len(items)):
		items[i]*=2
numbers=[10,3,7,1,9]
modify_elements(numbers)
print(numbers)

#Сортировка
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort()#по возрастания
numbers.sort(reverse=True)#по убыванию
asc_numbers=sorted(numbers)#новый сортированный список
asc_letters=sorted('based')
print(asc_letters)

#Поиск по последовательности
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print(numbers.index(3))#возвращает индекс 0

numbers*=2#записывает в переменную две копии списка
print(numbers.index(3,7))#Ищет первый аргумент, со индекса, равного второму аргумента
print(numbers.index(7,0,4))#Ищет первый аргумент, с индекса, равного второму аргумента и до индекса,равного третьему аргументу

#Проверка методом in и not in
print(3 in numbers)#Истина
print(7 not in numbers)#Ложь

key=1000

if key in numbers:
	print(f'{key} is in numbers')
else:
	print(f'{key} isn\'t in numbers')

#Изменение списка
colors=['orange','yellow','green']
colors.insert(0,'based')#вставка по индексу 
colors.append('blue')#вставка в конец
colors.extend(['pink','violet'])#вставка в конец всех элементов последовательности
colors.remove('green')#удаление по первому вхождению
colors.clear()#очищение списка
print(colors)


#Количество вхождений
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,
1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
print(responses.count(2))

colors=['red', 'orange', 'yellow', 'green', 'blue']
colors.reverse()#обратный порядок
print(colors)

#Копирование списка
copied=sorted(colors.copy())
print(copied)






