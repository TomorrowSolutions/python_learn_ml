#stack.py

"""
Моделирование стека на базе списка
"""

stack=[]

stack.append('yellow')
stack.append('green')
stack.append('red')

#pop возвращает последний элемент с конца
print(stack.pop())# red
print(stack.pop())# green
print(stack.pop())# yellow