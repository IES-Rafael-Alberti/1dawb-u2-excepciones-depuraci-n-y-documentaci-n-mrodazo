"""
P2.4 - Ejercicio.
El algoritmo burbuja
El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.

"""

def algoritmoBurbuja (a):
    total = len(a)-1

    #Bucle padre actua como contador
    for i in range (1, len(a)):
        #Bucle hijo actúa como comparador
        for j in range (0, total):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        total -= 1

        
#Meter un bucle para en lugar de mostrar del tirón la lista, que lo vaya haciendo poco a poco




def main ():
    a=[8, 3, 1, 19, 14]


if __name__ == "__main__":
    main()