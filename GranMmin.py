import pulp as lp

# Creamos un problema de minimización
prob = lp.LpProblem("Problema de minimización", lp.LpMinimize)

# Definimos las variables de decisión
x1 = lp.LpVariable("x1", lowBound=0)
x2 = lp.LpVariable("x2", lowBound=0)
x3 = lp.LpVariable("x3", lowBound=0)

# Definimos las variables de holgura y las variables artificiales
s1 = lp.LpVariable("s1", lowBound=0)
s2 = lp.LpVariable("s2", lowBound=0)
s3 = lp.LpVariable("s3", lowBound=0)
A1 = lp.LpVariable("A1", lowBound=0)
A2 = lp.LpVariable("A2", lowBound=0)
A3 = lp.LpVariable("A3", lowBound=0)

# Definimos la función objetivo
prob += 3*x1 + 7*x2 + 2*x3 + 1000*(A1 + A2 + A3)

# Definimos las restricciones
prob += x1 + x2 + 3*x3 - s1 + A1 >= 6
prob += x1 + 2*x2 + 2*x3 - s2 + A2 >= 7
prob += x1 + 3*x2 + 3*x3 - s3 + A3 >= 11

# Resolvemos el problema utilizando el solver GLPK
prob.solve(lp.GLPK())

# Imprimimos el resultado
print("Status:", lp.LpStatus[prob.status])
print("Solución óptima:")
print("x1 =", lp.value(x1))
print("x2 =", lp.value(x2))
print("x3 =", lp.value(x3))
print("Z =", lp.value(prob.objective))

# Verificamos que todas las variables de holgura y las variables artificiales son cero
print("Verificación de factibilidad:")
print("s1 =", lp.value(s1))
print("s2 =", lp.value(s2))
print("s3 =", lp.value(s3))
print("A1 =", lp.value(A1))
print("A2 =", lp.value(A2))
print("A3 =", lp.value(A3))
