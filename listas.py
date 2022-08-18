#--------------------Lista o Array --------------------

# [pos 0, pos 1, pos 2, .... , pos -1]

lista_numerica = [1,2,3,4]
lista_string =["hello","world", "hola","mundo", "ciao", "mundi", "ni hao","shijie"]
lista_variada = [1,-5,12.3,"string", lista_numerica]

# indice y slicing.

print("-"*90+"[indice y slicing]"+"-"*90)
print(lista_variada[1])
print(lista_numerica[1:])

# Concatenar

print("-"*90+"[Concatenar]"+"-"*90)
concatenacion = lista_numerica + lista_string
print(concatenacion)

# Mutabilidad

print("-"*90+"[Mutabilidad]"+"-"*90)
lista_numerica[2] = "mutable"
print(lista_numerica)

# Slicing lista[desde:hasta:salto]

print("-"*90+"[Slicing lista[desde:hasta:salto]]"+"-"*90)
valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valores[0:5])
print(valores[5:])
print(valores[2:-1:2])
print(valores[-1::-2])
print(valores[-1:0:-2])

# Asignacion 

print("-"*90+"[Asignacion]"+"-"*90)
valores[:3] = ["a", "b", "c"]
print(valores)

# Borrar

print("-"*90+"[Borrar]"+"-"*90)
valores[:3] = []
print(valores)

#--------------------FUNCIONES--------------------

print("*"*90+"[FUNCIONES]"+"*"*90) 

# APPEND ---> agregar un item al final de una lista.

print("-"*90+"[APPEND]"+"-"*90)
valores.append(1)
valores.append(2*4)
print(valores)

# LEN ---> devuelve longitud de una lista.

print("-"*90+"[LEN]"+"-"*90)
print(len(valores))

# POP ---> .pop () elimina el ultimo item de una lista y lo devuelve. .pop(valor) elimina el primer valor y lo devuelve.

print("-"*90+"[POP]"+"-"*90)
recipiente = valores.pop()
print(valores)
print(recipiente)

# COUNT ---> lista.count(item) cuenta el numero de veces que aparece el item

print("-"*90+"[COUNT]"+"-"*90)
valores += [1,2,1,2,1,2,1]
print(f"numero de 1: {valores.count(1)}")

# INDEX ---> .index(item) busca el item y devuelve la primera ubicacion en la que aparece.

print("-"*90+"[INDEX]"+"-"*90)
print(valores)
print(valores.index(1))

# Convertir una tupla a lista list()

print("-"*90+"[Convertir una tupla a lista list()]"+"-"*90)
numeros = (1,2,3,4)
print(numeros,type(numeros))
numeros = list(numeros)
print(numeros,type(numeros))

# Clear
print("-"*90+"[Clear]"+"-"*90)
numeros.clear()
print(numeros)
numeros = [1,2,3,4]
numeros= []
print(numeros)

# Extend
print("-"*90+"[Extend]"+"-"*90)
numeros = [1,2,3,4]
numeros.extend(valores)
print(numeros)

# Insert
print("-"*90+"[Insert]"+"-"*90)
numeros.insert(3,"en pos 4 agrego esto.")
print(numeros)

# Reverse
print("-"*90+"[Reverse]"+"-"*90)
numeros.reverse()
print(numeros)

# Sort
print("-"*90+"[Sort]"+"-"*90)
numeros.pop(-4) # borro el string..
numeros.sort()
print(numeros)



