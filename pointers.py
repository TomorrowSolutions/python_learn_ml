x=7
print(x)
print('id(x):',id(x))
def cube(number):
	print('id(number) before mod:',id(number))
	number **=3
	print('id(number) after mod:',id(number))
	return number
print(cube(x))
print('x=',x)