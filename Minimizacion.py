import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Definir la función objetivo y las restricciones
c = np.array([600, 40])
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 9])

# Resolver el problema de optimización
res = linprog(c, A_ub=-A, b_ub=-b, bounds=(0, None))

# Imprimir la solución óptima
print('Valor óptimo de la función objetivo:', res.fun)
print('Valor de x:', res.x[0])
print('Valor de y:', res.x[1])

# Creamos una malla de puntos para graficar las funciones
x = np.linspace(0, 10, 500)
y1 = (8 - 2*x)/1
y2 = (9 - 1*x)/3

# Creamos la figura y los ejes
fig, ax = plt.subplots(figsize=(8,6))

# Graficamos las restricciones
ax.plot(x, y1, label=r'$2x+y\geq 8$')
ax.plot(x, y2, label=r'$x+3y\geq 9$')
ax.axvline(x=0, color='black', lw=1.5)
ax.axhline(y=0, color='black', lw=1.5)
ax.legend(fontsize=12, loc='upper right')

# Sombrear el área factible
ax.fill_between(x, y1, y2, where=y2 >= y1, interpolate=True, alpha=0.2)

# Configuración de los ejes y etiquetas
ax.set_xlim(0, 4)
ax.set_ylim(0, 5)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$y$', fontsize=14)
ax.set_title('Área factible de un problema de programación lineal', fontsize=16)

plt.show()
