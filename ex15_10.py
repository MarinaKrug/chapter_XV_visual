import matplotlib.pyplot as plt
import numpy as np

from die import Die



die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# Визуализация результатов.

s = plt.figure()


list_numbers = np.array(frequencies)
colors = ['#4285b4', '#79a0c1', '#6c92af', '#78a2b7', '#007ba7', '#064b5c', '#003841', '#193737', '#1f3a3d', '#1f3438', '#293133']
explodes = [0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


s1 = plt.pie(list_numbers, autopct='%.2f', colors=colors, explode=explodes)
s1[2][0].set_color('white')


plt.show()
# Визуализация результатов.
