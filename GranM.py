# Importar la librería PuLP
import pulp as lp

# Crear un problema de maximización
prob = lp.LpProblem("Ejemplo", lp.LpMaximize)

# Crear las variables de decisión
x1 = lp.LpVariable("x1", lowBound=0)
x2 = lp.LpVariable("x2", lowBound=0)

# Agregar la función objetivo al problema
prob += 20*x1 + 40*x2

# Agregar las restricciones al problema
prob += 3*x1 + 5*x2 <= 240
prob += 2*x1 + 4*x2 <= 160

# Resolver el problema
prob.solve()

# Imprimir el estado del problema
print("Estado:", lp.LpStatus[prob.status])

# Imprimir los valores de las variables de decisión
print("x1 =", lp.value(x1))
print("x2 =", lp.value(x2))

# Imprimir el valor de la función objetivo
print("Valor objetivo =", lp.value(prob.objective))
