# Importar la librería PuLP
import pulp as lp

# Crear un problema de maximización
prob = lp.LpProblem("Ejemplo", lp.LpMinimize)

# Crear las variables de decisión
x1 = lp.LpVariable("x1", lowBound=0)
x2 = lp.LpVariable("x2", lowBound=0)
x3 = lp.LpVariable("x3", lowBound=0)

# Crear las variables de Holgura y Artificiales
s1 = lp.LpVariable("s1", lowBound=0)
s2 = lp.LpVariable("s2", lowBound=0)
s3 = lp.LpVariable("s3", lowBound=0)
A1 = lp.LpVariable("A1", lowBound=0)
A2 = lp.LpVariable("A2", lowBound=0)
A3 = lp.LpVariable("A3", lowBound=0)

# Agregar la función objetivo al problema
prob += 3*x1 + 7*x2 + 2*x3 + 1000*(A1 + A2 + A3)

# Agregar las restricciones al problema
prob += x1 + x2 + 3*x3 - s1 + A1 >= 6
prob += x1 + 2*x2 + 2*x3 - s2 + A2 >= 7
prob += x1 + 3*x2 + 3*x3 - s3 + A3 >= 11

# Resolver el problema
prob.solve()

# Imprimir el estado del problema
print("Estado:", lp.LpStatus[prob.status])
print("solución óptima:")

# Imprimir los valores de las variables de decisión
print("x1 =", lp.value(x1))
print("x2 =", lp.value(x2))
print("x3 =", lp.value(x3))
print("Z =", lp.value(prob.objective))

#verificamos que todas las variables de holgura y artificiales son cero
print("Verificación de Factibilidad:")
print("s1 =", lp.value(s1))
print("s2 =", lp.value(s2))
print("s3 =", lp.value(s3))
print("A1 =", lp.value(A1))
print("A2 =", lp.value(A2))
print("A3 =", lp.value(A3))
