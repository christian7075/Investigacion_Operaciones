# Importar la librería PuLP
import pulp as lp

# Crear un problema de maximización
prob = lp.LpProblem("Ejemplo", lp.LpMaximize)

# Crear las variables de decisión
x1 = lp.LpVariable("x1", lowBound=0)
x2 = lp.LpVariable("x2", lowBound=0)
x3 = lp.LpVariable("x3", lowBound=0)

# Crear las variables de Holgura y Artificiales
H1 = lp.LpVariable("H1", lowBound=0)
H2 = lp.LpVariable("H2", lowBound=0)
A1 = lp.LpVariable("A1", lowBound=0)
A2 = lp.LpVariable("A2", lowBound=0)

# Agregar la función objetivo al problema
prob += 30*x1 + 25*x2 + 40*x3

# Agregar las restricciones al problema
prob += 2*x1 + 2*x2 + 4*x3 + H1 == 60
prob += 3*x1 + 4*x2 + 6*x3 - H2 + A1 == 90
prob += 4*x1 + 2*x2 + 5*x3 + A2 == 100

# Resolver el problema
prob.solve()

# Imprimir el estado del problema
print("Estado:", lp.LpStatus[prob.status])

# Imprimir los valores de las variables de decisión
print("x1 =", lp.value(x1))
print("x2 =", lp.value(x2))
print("x3 =", lp.value(x3))

# Imprimir el valor de la función objetivo
print("Valor objetivo =", lp.value(prob.objective))

#verificamos que todas las variables de holgura y artificiales son cero
print("Verificación de Factibilidad:")
print("H1 =", lp.value(H1))
print("H2 =", lp.value(H2))
print("A1 =", lp.value(A1))
print("A2 =", lp.value(A2))
