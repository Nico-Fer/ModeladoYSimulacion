import numpy as np
from tabulate import tabulate
import math

def busqueda_binaria_raiz(f, a, b, iteraciones, precision, error):
    """
    Encuentra la raíz de una función utilizando el método de bisección (búsqueda binaria).
    
    Parámetros:
    f           : La función matemática a evaluar.
    a, b        : Los extremos del intervalo inicial [a, b].
    iteraciones : Cantidad máxima de iteraciones permitidas.
    precision   : Tolerancia para el tamaño del intervalo (b - a).
    error       : Tolerancia para el valor de f(c) cercano a 0.
    """

    if f(a) == 0.0:
        print(f"\n¡Éxito! La raíz exacta se encuentra en el extremo 'a': {a}")
        return a
    if f(b) == 0.0:
        print(f"\n¡Éxito! La raíz exacta se encuentra en el extremo 'b': {b}")
        return b
    
    # Comprobación inicial: la función debe cambiar de signo en el intervalo
    if f(a) * f(b) > 0:
        print("Error: La función no cambia de signo en el intervalo [a, b].")
        print("El método de bisección requiere que f(a) y f(b) tengan signos opuestos.")
        return None

    resultados = []
    
    for i in range(1, iteraciones + 1):
        # Calcular el punto medio (búsqueda binaria)
        c = (a + b) / 2.0
        fc = f(c)
        
        # Guardar los datos de esta iteración para la tabla
        resultados.append([i, a, b, c, fc, abs(b - a) / 2.0])
        
        # Criterios de parada: 
        # 1. El valor de la función es menor o igual al error buscado.
        # 2. La mitad del intervalo es menor o igual a la precisión.
        if abs(fc) <= error or (b - a) / 2.0 <= precision:
            break
            
        # Determinar el nuevo subintervalo
        if f(a) * fc < 0:
            b = c  # La raíz está en la mitad izquierda
        else:
            a = c  # La raíz está en la mitad derecha

    # Imprimir la tabla de iteraciones utilizando tabulate
    encabezados = ["Iteración", "a", "b", "c (Raíz aprox)", "f(c)", "Error (b-a)/2"]
    print(tabulate(resultados, headers=encabezados, floatfmt=".6f", tablefmt="grid"))
    
    print(f"\nRaíz encontrada: {c}")
    print(f"Iteraciones realizadas: {len(resultados)}")
    
    return c

# ==========================================
# Ejemplo de uso
# ==========================================
if __name__ == "__main__":
    # Definimos una función matemática usando numpy
    # Por ejemplo: f(x) = x^3 - x - 2 (Tiene una raíz real cerca de 1.521)
    def mi_funcion(x):
        return ((math.sqrt(x)-(math.cos(x))))

    # Parámetros de la búsqueda
    valor_a = 0.0
    valor_b = 1.0
    max_iteraciones = 50
    tolerancia_precision = 1e-3
    tolerancia_error = 1e-5

    print(f"Buscando la raíz de f(x) = x^3 - x - 2 en el intervalo [{valor_a}, {valor_b}]\n")
    
    # Llamada a la función
    raiz = busqueda_binaria_raiz(
        f=mi_funcion, 
        a=valor_a, 
        b=valor_b, 
        iteraciones=max_iteraciones, 
        precision=tolerancia_precision, 
        error=tolerancia_error
    )