#--------------------Lista o Array --------------------

# [pos 0, pos 1, pos 2, .... , pos -1]
lista_numerica = [1,2,3,4]
lista_string =["hello","world", "hola","mundo", "ciao", "mundi", "ni hao","shijie"]
lista_variada = [1,-5,12.3,"string", lista_numerica]

# indice y slicing.
print(lista_variada[1])
print(lista_numerica[1:])

# Concatenar
concatenacion = lista_numerica + lista_string
print(concatenacion)

# Mutabilidad
lista_numerica[2] = "mutable"
print(lista_numerica)

# Slicing lista[desde:hasta:salto]
valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valores[0:5])
print(valores[5:])
print(valores[2:-1:2])
print(valores[-1::-2])
print(valores[-1:0:-2])
# Asignacion 
valores[:3] = ["a", "b", "c"]
print(valores)
# Borrar
valores[:3] = []
print(valores)

#--------------------FUNCIONES--------------------

# APPEND ---> agregar un item al final de una lista.
valores.append(1)
valores.append(2*4)
print(valores)

# LEN ---> devuelve longitud de una lista.
print(len(valores))

# POP ---> .pop () elimina el ultimo item de una lista y lo devuelve. .pop(valor) elimina el primer valor y lo devuelve.
recipiente = valores.pop()
print(valores)
print(recipiente)

# COUNT ---> lista.count(item) cuenta el numero de veces que aparece el item
valores += [1,2,1,2,1,2,1]
print(f"numero de 1: {valores.count(1)}")

# INDEX ---> .index(item) busca el item y devuelve la primera ubicacion en la que aparece.
print(valores)
print(valores.index(1))

# Convertir una tupla a lista list()
numeros = (1,2,3,4)
print(numeros,type(numeros))
numeros = list(numeros)
print(numeros,type(numeros))
