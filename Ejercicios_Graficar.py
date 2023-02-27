import numpy as np
import matplotlib.pyplot as plt

# Definir los datos de la función
def f(x):
    return 5 - 2*x #Retornar la Funcion que se desee Graficar

x = np.linspace(-5, 5, 100)
y = f(x)

# Crear la figura de la gráfica
fig, ax = plt.subplots()

# Graficar la función
ax.plot(x, y, label='2x + y < 5')

# Sombrar la región factible
ax.fill_between(x, y, -5, where=(y >= -5), alpha=0.2)

# Personalizar la gráfica
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Función y área factible')
ax.legend()

# Mostrar la gráfica
plt.show()
