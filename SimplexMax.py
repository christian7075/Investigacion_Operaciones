from scipy.optimize import linprog
obj = [-4, -6]  # Coefficients of the objective function to be minimized
lhs_eq = [[2, 1]]  # Coefficients of the left-hand side of the equality constraint
rhs_eq = [5]  # Right-hand side of the equality constraint
res = linprog(c=obj, A_eq=lhs_eq, b_eq=rhs_eq, bounds=(0, None))
print(res)
