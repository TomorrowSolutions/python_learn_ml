#dispersion.py

"""
Расчет дисперсии
"""

import statistics,math

vals = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print('дисперсия=',statistics.pvariance(vals))
print('стандартное отклонение=',statistics.pstdev(vals))
print('стандартное отклонение=',math.sqrt(statistics.pvariance(vals)))