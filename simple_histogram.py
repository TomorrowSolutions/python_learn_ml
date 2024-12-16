#simple_histogram

"""
Построение примитивной	гистограммы из звездочек
"""

nums = [19,33,1,5,8]
print(f'Index{"Value":>8}   Bar')
for i,v in enumerate(nums):
	print(f'{i:>5}{v:>8}   {"*"*v}')