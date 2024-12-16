f = 1 

for i in range(5,0,-1):
	f*=i
print(f)

def factorial(number):
	"""Возвращает факториал числа"""
	if number <=1:
		return 1
	return number * factorial(number-1)#рекурсивный вызов
for i in range (11):
	print(f'{i}! = {factorial(i)}')