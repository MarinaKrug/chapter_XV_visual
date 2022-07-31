import matplotlib.pyplot as plt
import numpy as np


x_values = np.arange(1, 1001)
y_values = x_values**2
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(x_values, y_values)
# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)
# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

x_values = np.arange(1, 1001)
y_values = x_values**3
plt.style.use('seaborn')
fig1, ax1 = plt.subplots()

ax1.plot(x_values, y_values)
# Назначение заголовка диаграммы и меток осей.
ax1.set_title("Cube Numbers", fontsize=24)
ax1.set_xlabel("Value", fontsize=14)
ax1.set_ylabel("Cube of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax1.tick_params(axis='both', which='major', labelsize=14)


plt.show()
plt.savefig('fig_plot.png', bbox_inches='tight')