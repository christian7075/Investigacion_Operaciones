import numpy as np
import matplotlib.pyplot as plt
from pulp import *

# Crear el problema de maximización
prob = LpProblem("Maximización de P", LpMaximize)

# Definir las variables de decisión
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Definir la función objetivo
prob += 4*x + 6*y

# Agregar las restricciones
prob += 2*x + y <= 180
prob += x + 2*y <= 160
prob += x + y <= 100

# Resolver el problema
prob.solve()

# Imprimir la solución
print("x = ", value(x))
print("y = ", value(y))
print("P = ", value(prob.objective))

# Graficar las restricciones y la solución
x_vals = np.linspace(0, 100, 1000)
y_vals_1 = 180 - 2*x_vals
y_vals_2 = (160 - x_vals)/2
y_vals_3 = 100 - x_vals
y_vals_4 = np.maximum(0, (180 - 2*x_vals)/6)
y_vals_5 = np.maximum(0, (160 - x_vals)/4)
y_vals_6 = np.maximum(0, (100 - x_vals)/5)

fig, ax = plt.subplots()

ax.plot(x_vals, y_vals_1, label='2x + y = 180')
ax.plot(x_vals, y_vals_2, label='x + 2y = 160')
ax.plot(x_vals, y_vals_3, label='x + y = 100')

ax.fill_between(x_vals, y_vals_4, 100, where=(y_vals_4 <= y_vals_3) & (y_vals_4 <= y_vals_2), alpha=0.2)
ax.fill_between(x_vals, y_vals_5, y_vals_2, where=(y_vals_5 <= y_vals_3) & (y_vals_5 <= y_vals_1), alpha=0.2)
ax.fill_between(x_vals, y_vals_6, y_vals_1, where=(y_vals_6 <= y_vals_2) & (y_vals_6 <= 100), alpha=0.2)

ax.scatter(value(x), value(y), color='r', marker='o', label='Solución óptima')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Solución óptima')
ax.legend()

plt.show()
