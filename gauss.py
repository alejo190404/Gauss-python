from math import factorial

#Función para imprimir matriz en consola
def imprimirMatriz(matriz):
    print("Matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz) + 1):
            if(j == len(matriz)):
                print("|" + str(matriz[i][j]))
            else:
                print(matriz[i][j], end="\t")
        print()

#Función para imprimir soluciones con formato
def imprimirSoluciones(soluciones):
    print("Soluciones:")
    for i in range(len(soluciones)):
        print("x" + str(i + 1) + " = " + str(soluciones[i]))

#Función para transformar una fila de la matriz
def transformarFila(matriz, Fpivot, Ftransform, factor):
    for i in range(len(matriz) + 1):
        matriz[Ftransform][i] = matriz[Ftransform][i] - (matriz[Fpivot][i] * factor)

#Función para aplicar algorimto de Gauss
def gauss(matrix, n):
    for i in range(n):
        if (matrix[i][i]==0):
            return i #Devuelve el número de iteración en la cual se encontró el pivote 0, para que otra función realice el cambio de fila
        for j in range(n-i-1):
            factor = matrix[j+i+1][i]/matrix[i][i]
            transformarFila(matrix, i, j+i+1, factor)
        imprimirMatriz(matrix)
    return -1 #Devuelve -1 si en esta iteración de Gauss, no se requirió realizar más cambios de fila

#Función para cambiar filas dentro de la matriz

def cambiarFilasMatriz(matriz, Fproblema):
    n = len(matriz)
    if (n == Fproblema):
        print("El sistema de ecuaciones no se pudo resolver. Asegúrese que esté bien escrito y que las ecuaciones tengan independencia lineal")
        imprimirMatriz(matriz)
        exit()
    else:
        aux = matriz[Fproblema]
        matriz[Fproblema] = matriz[Fproblema + 1]
        matriz[Fproblema + 1] = aux
        return matriz



#Comienzo del programa
print("Ingresa el numero de variables")

n = int(input())

matrix = []

print("Ingresa el sistema de ecuaciones en forma de matriz extendida")

for i in range(n):
    row = []
    for j in range(n + 1): #n + 1 para incluir la solución
        print("Ingresa el elemento [" + str(i) + "][" + str(j) + "]")
        row.append(int(input()))
    matrix.append(row)

#Aplicar algoritmo de Gauss
for i in range(n):
    problema = gauss(matrix, n)
    if (problema != -1):
        matrix = cambiarFilasMatriz(matrix, problema)
        imprimirMatriz(matrix)
    else:
        break



print("Resultado final: ")
imprimirMatriz(matrix)


#Despejar ecuaciones reempleazando "hacia atrás"
soluciones =[]
for i in range(n):
    soluciones.append(1)

for i in range(n):
    if (matrix[-(i+1)][-(i+2)]==1):
        suma = 0
        for j in range(n):
            suma += matrix[-(i+1)][j]*soluciones[j]
        suma = suma - 1
        soluciones[-(i+1)] = matrix[-(i+1)][-1] - suma

    else:
        divisor = matrix[-(i+1)][-(i+2)]
        for j in range(n+1):
            matrix[-(i+1)][j] = matrix[-(i+1)][j]/divisor
        suma = 0
        for j in range(n):
            suma += matrix[-(i+1)][j]*soluciones[j]
        suma = suma - 1
        soluciones[-(i+1)] = matrix[-(i+1)][-1] - suma


#Imprimir matriz para confirmar
imprimirMatriz(matrix)
#Imprimir soluciones con formato
imprimirSoluciones(soluciones)


#Comentario de prueba
