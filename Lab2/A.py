import numpy as np
from scipy.optimize import linprog


c = [-21, -69, -44, -39]


A_ub = [
    [0, 2, 1, 1],  
    [3, 3, 0, 6],  
    [2, 3, 0, 2],  
    [4, 6, 0, 5],  
    [3, 1, 5, 4],  
]


b_ub = [929, 410, 507, 865, 425]

x_bounds = [(0, None), (0, None), (0, None), (0, None)]


res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method="highs")


print("Статус:", res.message)
print(f"x1 (Astro) = {res.x[0]:.2f} шт.")
print(f"x2 (Cosmo) = {res.x[1]:.2f} шт.")
print(f"x3 (Nova)  = {res.x[2]:.2f} шт.")
print(f"x4 (Vega)  = {res.x[3]:.2f} шт.")
print(f"Максимальний прибуток = {-res.fun:.2f} грн")