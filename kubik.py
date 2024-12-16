#kubik.py
'''6 000 000 бросков игрального кубика'''

import random

#счетчики соответствующих граней
freq1=0
freq2=0
freq3=0
freq4=0
freq5=0
freq6=0

#цикл на 6 миллионов бросков
for roll in range(6_000_000):
	face=random.randrange(1,7)

	#увеличение соответствующего счетчика
	if face == 1:
		freq1+=1
	elif face ==2:
		freq2+=1
	elif face ==3:
		freq3+=1
	elif face ==4:
		freq4+=1
	elif face ==5:
		freq5+=1
	elif face ==6:
		freq6+=1
print(f'{"Сторона":>4}{"Кол-во выпаданий":>20}')
print(f'{1:>4}{freq1:>20}')
print(f'{2:>4}{freq2:>20}')
print(f'{3:>4}{freq3:>20}')
print(f'{4:>4}{freq4:>20}')
print(f'{5:>4}{freq5:>20}')
print(f'{6:>4}{freq6:>20}')