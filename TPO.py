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

def camino_valido(tablero, movs=0, n=2, mov=[], a=[]):
    # Si hemos alcanzado todos los movimientos necesarios, imprimimos el tablero
    if movs == (n * n)-1:
        imprimir(tablero)
        return True
    # Intentamos cada movimiento posible
    for i in range(8):
        x, y = a[0] + mov[i][0], a[1] + mov[i][1]
        # Verificar que la posición es válida y no ha sido visitada
        if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] == 0:
            tablero[x][y] = movs + 2
            #imprimir(tablero)
            #print()
            # Llamada recursiva: si se encuentra un camino válido, detener la búsqueda
            if camino_valido(tablero, movs + 1, n, mov, [x, y]):
                return True
            # Restaurar el tablero si el camino no es válido
            tablero[x][y] = 0

    return False

def camino_valido_opt(tablero, movs=0, n=8, mov=[], a=[], camino=[]):
    # Agregar la posición actual al camino
    camino.append(a)

    # Si hemos alcanzado todos los movimientos necesarios, marcamos el tablero con el camino encontrado
    if movs == n * n - 1:
        for paso, (x, y) in enumerate(camino):
            tablero[x][y] = paso + 1
        imprimir(tablero)
        return True  # Termina al encontrar la solución completa

    # Intentar cada movimiento en el orden dado
    for dx, dy in mov:
        x, y = a[0] + dx, a[1] + dy
        if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] == 0:
            if camino_valido_opt(tablero, movs + 1, n, mov, [x, y], camino):
                return True

    # Retiramos la posición del camino si no encontramos solución con ella
    camino.pop()
    return False

# Main:
n = int(input("Ingrese el tamaño del tablero: "))
x = int(input("Ingrese la coordenada en las filas: "))
y = int(input("Ingrese la coordenada en las columnas: "))

a = [x-1, y-1]
mov = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
tablero = []
camino=[]
crear_tablero(n, tablero, a)

if camino_valido(tablero, 0, n, mov, a)==False:
    print("No hay solucion")

#if camino_valido_opt(tablero,0,n,mov,a,camino)==False:
#    print("No hay solucion")
