

def rectangle_area(length=2,width=3):
	"""Возвращает площадь прямоугольника"""
	return length*width
def average(*args):
	"""Среднее арифметическое набора"""
	return sum(args)/len(args)
digits=[1,2,3,4,5,6,7,8,9]
#print(average(*digits))
a = 'hello'	
def access_global():
	print(f'access to global variable a = {a}')
def try_modify_global():
	a='alloha'
	print(f'trying to modify a = {a}')
def modify_global():
	global x
	x='alloha'
	print(f'x modified from modify_global:{x}')


e='hola'

from math import *
import statistics as stat
print(floor(10.7))
grades=[1,2,3,4,5,5,6,7,8,9]
print(stat.mean(grades))
print(e)

