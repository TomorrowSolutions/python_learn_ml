#kraps.py
"""Моделирование игры крэпс."""

"""
Правила:

Игрок бросает два шестигранных кубика, на грани которых нанесены 1, 2, 3,
4, 5 или 6 очков. Когда кубики останавливаются, вычисляется сумма очков
на двух верхних гранях. Если при первом броске выпадает 7 или 11, игрок
побеждает. Если при первом броске сумма равна 2, 3 или 12 («крэпс»), игрок
проигрывает (побеждает «казино»). Если при первом броске сумма равна 4,
5, 6, 8, 9 или 10, то она становится «целью» игрока. Чтобы победить, игрок
должен на последующих бросках выбросить то же целевое значение. Если
перед этим игрок выбросит 7, он проигрывает.

"""



import random

def roll_dice():
	"""Моделирует бросок двух кубиков и возвращает результат в виде кортежа"""
	roll1 = random.randrange(1,7)
	roll2 = random.randrange(1,7)
	return (roll1,roll2)
def display_dice(dice):
	"""Выводит результат броска двух кубиков"""
	roll1,roll2 = dice #распаковка кортежа в две переменные
	print(f'Сумма броска {roll1} + {roll2} = {sum(dice)}')

roll_values = roll_dice()
display_dice(roll_values)

sum_of_dice = sum(roll_values)

if sum_of_dice in (7,11):#победа
	game_status='win'
elif sum_of_dice in (2,3,12):#проигрыш
	game_status='loose'
else: #цель
	game_status='continue'
	my_point=sum_of_dice
	print("Цель:",my_point)

while game_status == 'continue':
	roll_values = roll_dice()
	display_dice(roll_values)
	sum_of_dice=sum(roll_values)

	if sum_of_dice == my_point:
		game_status='win'
	elif sum_of_dice == 7:
		game_status='loose'

# Вывод результатов игры
if game_status == 'win':
	print('Победа')
else:
	print('Поражение')
