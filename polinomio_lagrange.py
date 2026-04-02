import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

def polinomio_lagrange(x, x_puntos, y_puntos):
    """
    Construye el polinomio P(x) como una suma ponderada de polinomios base L_i(x).
    Basado en la fórmula P(x) = Σ y_i * L_i(x).
    """
    n = len(x_puntos)
    P = 0
    for i in range(n):
        # Calcular el polinomio base de Lagrange L_i(x)
        li = 1
        for j in range(n):
            if i != j:
                # L_i(x) vale 1 en x_i y 0 en los demás puntos
                li *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        P += y_puntos[i] * li
    return P

def obtener_polinomio_simbolico(x_puntos, y_puntos):
    """
    Construye y devuelve la expresión algebraica del polinomio.
    Basado en el Teorema Fundamental de la Interpolación[cite: 48, 318].
    """
    x = sp.symbols('x')
    n = len(x_puntos)
    P_x = 0
    
    for i in range(n):
        # Construcción del polinomio base L_i(x) simbólico [cite: 31, 289]
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        
        # Suma ponderada simbólica: Σ y_i * L_i(x) [cite: 22, 281]
        P_x += y_puntos[i] * L_i
        
    # .simplify() expande y agrupa términos para mostrar el polinomio estándar
    return sp.simplify(P_x)

def f_ejemplo(x):
    """Función real para el experimento: e^x."""
    return np.exp(x)

def calcular_cota_error(x_eval, x_puntos, n, m_derivada):
    """
    Calcula la cota superior del error basada en la (n+1)-ésima derivada.
    Fórmula: |E(x)| <= (M_{n+1} / (n+1)!) * |Π(x - x_i)|.
    """
    # Término del producto Π(x - x_i)
    producto_distancias = 1
    for xi in x_puntos:
        producto_distancias *= (x_eval - xi)
    
    # Factorial (n+1)!
    factorial_n1 = math.factorial(n + 1)
    
    return (m_derivada / factorial_n1) * abs(producto_distancias)

def calcular_cotas(x_datos, y_datos):
    return 0

def main():
    # 1. Configuración de datos iniciales
    # Para e^x, todas sus derivadas son e^x. 
    # En el intervalo [0, 2], el valor máximo de la derivada (M) es e^2.
    x_datos = np.array([1,2,3]) 
    y_datos = f_ejemplo(x_datos)
    n = len(x_datos) - 1 # Grado del polinomio

    polinomio_expr = obtener_polinomio_simbolico(x_datos, y_datos)
    
    # M es el máximo de la (n+1)-ésima derivada en el intervalo
    M_n_plus_1 = np.exp(max(x_datos)) 
    
    # 2. Punto de evaluación para el error
    x_test = 2.5
    val_real = f_ejemplo(x_test)
    val_interp = polinomio_lagrange(x_test, x_datos, y_datos)
    
    # 3. Cálculo de errores
    # Error Local: Diferencia absoluta entre realidad y modelo
    error_local = abs(val_real - val_interp)
    
    # Error Global: Cota máxima teórica
    cota_global = calcular_cota_error(x_test, x_datos, n, M_n_plus_1)

    print(f"\nPolinomio Reconstruido P(x):")
    print(polinomio_expr)
    
    # 4. Mostrar resultados
    print(f"--- Análisis de Interpolación para e^x ---")
    print(f"Puntos de datos (nodos): {x_datos}")
    print(f"Evaluación en x = {x_test}:")
    print(f"  Valor Real f(x):       {val_real:.8f}")
    print(f"  Valor Interpolado P(x): {val_interp:.8f}")
    print(f"  Error Local Real:      {error_local:.2e}")
    print(f"  Cota de Error Global:   {cota_global:.2e}")
    
    if error_local <= cota_global:
        print("\nConfirmación: El error real está dentro de la cota teórica.")


if __name__ == "__main__":
    main()