"""
Con este ejemplo vemos que con el "for" no se modifica la lista, sólo muestra

"""

colores= ['a', 'b', 'c']

print (colores)

#Lo que hace es decir que color existe y va cogiendo cada elemento
for color in colores: 
    color='d'
print(colores)

for color in colores: 
    color='d'
print(colores)


"""
Con este ejemplo vemos que una lista tiene elementos iterables y otros métodos

"""

miLista = [1, 2, 3, 4]

print(miLista)

miLista = list(range(1, 5))

print(miLista)

miLista = list([1, 2, 3, 4])

print(miLista)

miLista.reverse()

print(miLista)


#Al poner el .sort lo que nos estamos es cargando la lista ya que eso devuelve None
miLista = miLista.sort()

print(miLista)
