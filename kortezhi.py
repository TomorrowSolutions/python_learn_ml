#kortezhi.py

"""
Тестирование кортежей (неизменяемый список)
"""

student_tuple='john','doe',3.3
print(student_tuple)
a_singleton_tuple= ('red',)#кортеж из одного элемента сопровождается запятой
print(a_singleton_tuple)

time_tuple= (9,16,1)

sec_from_midnight = time_tuple[0]*3600+time_tuple[1]*60 +time_tuple[2]
print(sec_from_midnight)

#Изменение кортежей

t1 = (10,20,30)
t2=t1
t1+=(40,50)
print(t1)#Расширенный
print(t2)#Исходный

#Список внутри кортежа можно изменить
t3 = ('jared','deer',[1,2,3])
t3[2][2]=4
print(t3)

#Распаковка кортежа
student_tuple='john',21
student_name,student_age=student_tuple
print(f'student {student_name} is {student_age}')
#Распаковка строки
first,second ='hi'
print(first,second)
#Распаковка range
n1,n2,n3 = range(10,40,10)
print(n1,n2,n3)

#Безопасный перебор индексов и значений enumerate
colors=['red','orange','yellow']
for i,v in enumerate(colors):
	print(f'{i}:{v}')

