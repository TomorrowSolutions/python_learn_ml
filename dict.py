"""
 Словари и манипуляции с ними
"""

from collections import Counter

country_code={'Belarus':'by',
'Russia':'ru','Kazahstan':'kz'
}
#Не пустой словарь интерпретируется как true
if country_code:
	print("SNG")

roman_nums = {
	'I':1,
	'II':2,
	'III':3,
	'IV':4,
	'V':10
}
#Обращение по ключу
print(roman_nums['V'])
roman_nums['V']=5
print(roman_nums['V'])
#новый ключ
roman_nums['L']=50
print(roman_nums)
del roman_nums['L']
print(roman_nums)
#Безопасный поиск по ключу
print(roman_nums.get('baza'))
print('V' in roman_nums)
#ключи
for k in roman_nums.keys():
	print(k,end=' ')
print()
for v in roman_nums.values():
	print(v,end=' ')
capitals1={'Russia':'Moscow',
'Turkey':'Ankara'
}
capitals2={
'Turkey':'Ankara',
'Russia':'Moscow'
}
print()
print(capitals1==capitals2)

def unique_words(text):
	"""Выводит слово и его количество в тексте. В конце выводит количество уникальных слов"""
	word_counts={}
	for word in text.split():
		if word in word_counts:
			word_counts[word]+=1
		else:
			word_counts[word]=1
	print(f'{"WORD":<12}COUNT')
	for word,count in sorted(word_counts.items()):
		print(f'{word:<12}{count}')
	print('\nUnique words numer is ',len(word_counts))

def unique_counter(text):
	counter=Counter(text.split())
	for word,count in sorted(counter.items()):
		print(f'{word:<12}{count}')
	print('\nUnique words numer is ',len(counter.keys()))

text=('quick brown fox jumps over lazy dog '
'lazy dog stay quiet cause its tired of quick brown fox'
	)
unique_words(text)
unique_counter(text)
#Изменение методом update
country_code={}
country_code.update({'Russia':'ru'})
country_code.update(Belarus='by')
country_code.update(Belarus='ru')
print(country_code)
#Трансформация словарей 
grades = {'Yana': [99, 87, 94], 'Roman': [84, 95, 91]}
grades2 = {k:sum(v)/len(v) for k,v in grades.items()}
print(grades2)