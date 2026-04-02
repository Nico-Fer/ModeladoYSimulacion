import math
import numpy as np
import matplotlib.pyplot as plt

"""
f(x)=cos(x)
0=cos(x)
x= cos(x)+x
"""

def f(x):
    return (2*math.pow(math.e, math.pow(x, 2))-5*x)

def g(x):
    return 0.4*math.pow(math.e, math.pow(x, 2))

def fixed_point_iteration(x0, tol=1e-5, max_iter=200):
    x = x0
    iter_values = [x0]
    errors = [None]
    
    for i in range(max_iter):
        x_new = g(x)
        error = abs(x_new - x)

        iter_values.append(x_new)
        errors.append(error)
        
        if error < tol:
            print("Tolerancia alcanzada...")
            break
            
        x = x_new
        
    return x_new, iter_values, errors

def main():
    x0 = 0.0 # Valor inicial
    root, iter_values, errors = fixed_point_iteration(x0)

    # Graficar la función original y el proceso de iteración
    x_vals = np.linspace(-1, 0, 400)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label='$f(x)$')
    plt.scatter(iter_values, [f(x) for x in iter_values], color='red', zorder=5)
    plt.plot(iter_values, [f(x) for x in iter_values], color='red', linestyle='--', zorder=5)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title('Método del Punto Fijo para $f(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.legend()
    plt.show()

    print("-" * 40)
    print(f"La raíz aproximada es : {root:.6f}")
    print(f"Iteraciones totales   : {len(iter_values) - 1}")
    print(f"Error final           : {errors[-1]:.8f}")
    print("-" * 40)

if __name__ == "__main__":
    main()