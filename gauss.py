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

#Función para transformar una fila de la matriz
def transformarFila(matriz, Fpivot, Ftransform, factor):
    for i in range(len(matriz) + 1):
        matriz[Ftransform][i] = matriz[Ftransform][i] - (matriz[Fpivot][i] * factor)



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
imprimirMatriz(matrix)
for i in range(n):
    if (matrix[i][i]==0):
        print("La matriz tiene un pivote en 0. Asegúrese que el primer elemnto no sea 0, que las ecuaciones tengan independencia lienal o ingrese la matriz en otro orden")
        exit()
    for j in range(n-i-1):
        factor = matrix[j+i+1][i]/matrix[i][i]
        transformarFila(matrix, i, j+i+1, factor)
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
        for j in range(n+1):
            matrix[-(i+1)][j] = matrix[-(i+1)][j]/matrix[-(i+1)][-(i+2)]
            print("Operación ")
            imprimirMatriz(matrix)
        suma = 0
        for j in range(n):
            suma += matrix[-(i+1)][j]*soluciones[j]
        suma = suma - 1
        print("Operación ")
        print("SUma:  " + str(suma))
        imprimirMatriz(matrix)
        soluciones[-(i+1)] = matrix[-(i+1)][-1] - suma
    print("Iteración " + str(i))
    imprimirMatriz(matrix)
    print(soluciones)

imprimirMatriz(matrix)
print(soluciones)



#Imprimir matriz para confirmar
