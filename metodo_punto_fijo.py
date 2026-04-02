import math
import numpy as np
import matplotlib.pyplot as plt

"""
f(x)=cos(x)
0=cos(x)
x= cos(x)+x
"""

def f(x):
    return (math.pow(x,3) - x - 1)

def g(x):
    return math.pow(x+1, 1/3)

def fixed_point_iteration(x0, tol=1e-5, max_iter=200, dominio=None):
    x = x0
    iter_values = [x0]
    errors = [None]
    
    for i in range(max_iter):
        x_new = g(x)
        error = abs(x_new - x)

        # Verificación opcional del dominio acotado
        if dominio is not None:
            if not (dominio[0] <= x_new <= dominio[1]):
                print(f"\n¡Advertencia! El método divergió y salió del dominio {dominio} en la iteración {i+1}.")
                print(f"Valor calculado: x = {x_new:.6f}")
                # Retornamos lo calculado hasta ahora antes de romper el programa
                return None, iter_values, errors

        iter_values.append(x_new)
        errors.append(error)
        
        if error < tol:
            print("Tolerancia alcanzada...")
            break
            
        x = x_new
        
    return x_new, iter_values, errors

def main():
    x0 = 1 # Valor inicial
    root, iter_values, errors = fixed_point_iteration(x0, dominio=(1,2))

    print("-" * 40)
    if root is not None:
        print(f"La raíz aproximada es : {root:.6f}")
    else:
        print("No se encontró una raíz dentro del dominio especificado.")
    print(f"Iteraciones totales   : {len(iter_values) - 1}")
    if errors[-1] is not None:
        print(f"Error final           : {errors[-1]:.8f}")
    print("-" * 40)

if __name__ == "__main__":
    main()