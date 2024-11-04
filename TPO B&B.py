import time
def crear_tablero(n, tablero, a):
    for i in range(n):
        fila = [0] * n  # Crear una fila de n ceros
        tablero.append(fila)  # Agregar la fila al tablero
    tablero[a[0]][a[1]] = 1  # Marcar la posición inicial

def imprimir(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(f"|{x[i][j]:3d}", end=" ")
        print()

# Función para contar movimientos futuros desde una posición dada
def movimientos_disponibles(tablero, x, y, mov):
    n = len(tablero)
    count = 0
    for i in range(8):
        nx, ny = x + mov[i][0], y + mov[i][1]
        if 0 <= nx < n and 0 <= ny < n and tablero[nx][ny] == 0:
            count += 1
    return count

# Función que aplica la heurística de advertencia mínima (Warnsdorff's rule)
def camino_valido(tablero, movs=0, mov=[], a=[]):
    n = len(tablero)
    if movs == n * n - 1:
        imprimir(tablero)
        print("--- %s seconds ---" % (time.time() - tiempo))
        return True
    
    # Generar lista de movimientos posibles junto con el número de opciones futuras
    posibles_movs = []
    for i in range(8):
        x, y = a[0] + mov[i][0], a[1] + mov[i][1]
        if 0 <= x < n and 0 <= y < n and tablero[x][y] == 0:
            futuros_movs = movimientos_disponibles(tablero, x, y, mov)
            posibles_movs.append((futuros_movs, x, y))
    
    # Ordenar movimientos posibles por número de futuros movimientos (menor a mayor)
    posibles_movs.sort()
    
    # Intentar cada movimiento en el orden establecido por la heurística
    for _, x, y in posibles_movs:
        tablero[x][y] = movs + 2
        if camino_valido(tablero, movs + 1, mov, [x, y]):
            return True
        tablero[x][y] = 0

    return False

n = int(input("Ingrese el tamaño del tablero: "))
x = int(input("Ingrese la coordenada en las filas: "))
y = int(input("Ingrese la coordenada en las columnas: "))

a = [x - 1, y - 1]  # Ajustar índices para comenzar desde 0
mov = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
tablero = []
tiempo = time.time()
crear_tablero(n, tablero, a)
if not camino_valido(tablero, 0, mov, a):
    print("No hay solución")
    print("--- %s seconds ---" % (time.time() - tiempo))
