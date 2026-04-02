import numpy as np

def punto_fijo_con_aitken_tabla(g, x0, tol=1e-6, max_iter=100):
    """
    Método del punto fijo con aceleración de Aitken que muestra una tabla de iteraciones.
    g: función de iteración (polinomio en este caso).
    x0: aproximación inicial.
    tol: tolerancia para la convergencia.
    max_iter: número máximo de iteraciones.
    """
    x = x0
    print(f"{'Iteración':<10}{'x':<20}{'x1 = g(x)':<20}{'x2 = g(x1)':<20}{'x_acelerado':<20}{'Error':<20}")
    print("-" * 100)
    
    for i in range(max_iter):
        # Calcular tres puntos consecutivos de la iteración
        x1 = g(x)
        x2 = g(x1)
        
        # Aplicar la aceleración de Aitken
        denominador = x2 - 2 * x1 + x
        if denominador != 0:
            x_acelerado = x - (x1 - x)**2 / denominador
        else:
            x_acelerado = x2 # Si no se puede aplicar Aitken, continuar con x
            
        # Calcular error relativo
        error = abs(x_acelerado - x)
        
        # Mostrar valores en la tabla
        print(f"{i + 1:<10}{x:<20.10f}{x1:<20.10f}{x2:<20.10f}{x_acelerado:<20.10f}{error:<20.10f}")
        
        # Verificar convergencia
        if error < tol:
            print(f"\nConvergencia alcanzada en la iteración {i + 1}.")
            return x_acelerado
            
        # Actualizar para la siguiente iteración
        x = x_acelerado
        
    print("\nEl método no converge después del número máximo de iteraciones.")
    return None

# Función auxiliar a evaluar
def g(x):
    return np.cos(x) 
"""(2 * x - 1)**(1/2)"""

def main():
    # Parámetros de ejemplo
    x0 = 0.5 # Aproximación inicial
    
    # Ejecutar el método
    resultado = punto_fijo_con_aitken_tabla(g, x0)

    # Mostrar resultado final
    if resultado is not None:
        print(f"\nLa solución aproximada es: {resultado}")

# Punto de entrada del script
if __name__ == "__main__":
    main()