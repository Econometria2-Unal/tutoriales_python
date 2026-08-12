"""
Universidad Nacional de Colombia
Facultad de Ciencias Economicas

Econometria II | Tutoriales Python
Sesion: Recursion, iteración, scopes, debugger y complejidad computacional
        Ejemplo - Sucesión de Fibonacci

Semestre: 2026-1

Objetivo:
Comparar dos maneras de calcular números de la sucesión de Fibonacci:
una solución recursiva y una solución iterativa.
"""

# ===
# Tabla de contenidos
# ===

# 1. Función para calcular los números de Fibonacci de manera recursiva
# 2. Función para calcular los números de Fibonacci de manera iterativa

# Nota: Tips prácticos en Python
## Para limpiar el entorno en IPython/Jupyter se puede correr: "%reset -f"
## Para cerrar todas las gráficas actualmente abiertas: "plt.close('all')"
## En VS Code o Spyder, los bloques marcados con "# %%" se ejecutan por celdas.

# %% =========================
# 1. Función para calcular los números de Fibonacci de manera recursiva
# ============================

# Nota: "fibonacci_recursivo" es una función recursiva porque se llama a sí misma.

# Definición de la función "fibonacci_recursivo"
def fibonacci_recursivo(n):
    """Calcula el n-ésimo número de la sucesión de Fibonacci usando recursión.

    Parámetros
    ----------
    n : int
        Posición del número de Fibonacci que se quiere calcular. Se espera que
        sea un entero mayor o igual que 0.

    Retorna
    -------
    int
        Número de Fibonacci ubicado en la posición n.
    """
    
    # Los casos base detienen la recursión y representan los dos primeros
    # números de la sucesión de Fibonacci.
    
    # Caso base "n == 0"
    if n == 0:
        return 0
    # Caso base "n == 1"
    elif n == 1:
        return 1
    # Caso recursivo 
    else:
        # Para n >= 2, Fibonacci se define como la suma de los dos valores anteriores.
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    
# Nota: Problema de este enfoque recursivo, la complejidad computacional es O(2^{n}), entonces el algoritmo escala muy mal
#       a medida que "n" crece
#       Lo anterior, se puede mejorar usando una estructura de datos que almacene cálculos que se hicieron, reduciendo la
#       complejidad computacional de éste enfoque recursivo

# Se llama la función "fibonacci_recursivo" que se acaba de crear previamente.
f_rec = fibonacci_recursivo(8)

# Esta llamada ilustra el costo de la versión recursiva simple cuando n crece.
f_rec2 = fibonacci_recursivo(45)

# Se imprimen los resultados de la función
print(f_rec)
print(f_rec2)

# %% =========================
# 2. Función para calcular los números de Fibonacci de manera iterativa
# ============================

# Definición de la función "fibonacci_iterativo"
def fibonacci_iterativo(n):
    """Calcula el n-ésimo número de la sucesión de Fibonacci usando iteración.

    Parámetros
    ----------
    n : int
        Posición del número de Fibonacci que se quiere calcular. Se espera que
        sea un entero mayor o igual que 0.

    Retorna
    -------
    int
        Número de Fibonacci ubicado en la posición n.
    """
    # Condiciones iniciales (2 primeros números de la sucesión de Fibonacci)
    a = 0
    b = 1

    # En cada iteración se avanza una posición en la sucesión:
    # "a" guarda el valor actual y "b" guarda el siguiente valor.
    for i in range(n):    # i itera sobre todos los valores de range(n)
        # Condición de actualización. El "a" previo lo sistituimos por "b" y el 
        # "b" previo lo sistituimos por "a + b", siguiendo la misma lógica,
        #  que la sucesión de Fibonacci.
        a, b = b, a + b   

    # Al terminar el ciclo, "a" contiene el número de Fibonacci en la posición n.
    return a

# Se calcula el mismo ejemplo con la versión iterativa para comparar resultados.
f_iter = fibonacci_iterativo(8)
f_iter2 = fibonacci_iterativo(45)

# Se imprimen los resultados de la función
print(f_iter)
print(f_iter2)
