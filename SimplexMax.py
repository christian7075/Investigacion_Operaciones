from scipy.optimize import linprog
obj = [-4, -6]  # Coeficioentes de la funcion objetivo a ser maximizado
lhs_eq = [[2, 1]]  # Coeficientes de mano izquierda de la igualdad
rhs_eq = [5]  # Coeficientes de mano derecha de la igualdad
res = linprog(c=obj, A_eq=lhs_eq, b_eq=rhs_eq, bounds=(0, None))
print(res)
