##################################################################--------------------Lista o Array --------------------

################################################################## [pos 0, pos 1, pos 2, .... , pos -1]

lista_numerica = [1,2,3,4]
lista_string =["hello","world", "hola","mundo", "ciao", "mundi", "ni hao","shijie"]
lista_variada = [1,-5,12.3,"string", lista_numerica]

print("-"*90+"[indice y slicing]"+"-"*90) ################################################################## indice y slicing.

print(lista_variada[1])
print(lista_numerica[1:])

print("-"*90+"[Concatenar]"+"-"*90) ################################################################## Concatenar

concatenacion = lista_numerica + lista_string
print(concatenacion)

print("-"*90+"[Mutabilidad]"+"-"*90) ################################################################## Mutabilidad

lista_numerica[2] = "mutable"
print(lista_numerica)

print("-"*75+"[Slicing lista[desde:hasta:salto]]"+"-"*75) ############################################## Slicing lista[desde:hasta:salto]

valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valores[0:5])
print(valores[5:])
print(valores[2:-1:2])
print(valores[-1::-2])
print(valores[-1:0:-2])

print("-"*90+"[Asignacion]"+"-"*90) ################################################################## Asignacion 

valores[:3] = ["a", "b", "c"]
print(valores)

print("-"*90+"[Borrar]"+"-"*90) ################################################################## Borrar

valores[:3] = []
print(valores)

print("")
print("*"*90+"[FUNCIONES]"+"*"*90)  ##################################################################--------------------FUNCIONES--------------------
print("")

print("-"*90+"[APPEND]"+"-"*90) ################################################################## APPEND ---> agregar un item al final de una lista.

valores.append(1)
valores.append(2*4)
print(valores)

print("-"*90+"[LEN]"+"-"*90) ################################################################## LEN ---> devuelve longitud de una lista.

print(len(valores))

print("-"*90+"[POP]"+"-"*90) ################################################################## POP ---> .pop () elimina el ultimo item de una lista y lo devuelve. .pop(valor) elimina el primer valor y lo devuelve.

recipiente = valores.pop()
print(valores)
print(recipiente)

print("-"*90+"[COUNT]"+"-"*90) ################################################################## COUNT ---> lista.count(item) cuenta el numero de veces que aparece el item

valores += [1,2,1,2,1,2,1]
print(f"numero de 1: {valores.count(1)}")

print("-"*90+"[INDEX]"+"-"*90) ################################################################## INDEX ---> .index(item) busca el item y devuelve la primera ubicacion en la que aparece.

print(valores)
print(valores.index(1))

print("-"*80+"[Convertir una tupla a lista list()]"+"-"*80) #################################################### Convertir una tupla a lista list()

numeros = (1,2,3,4)
print(numeros,type(numeros))
numeros = list(numeros)
print(numeros,type(numeros))

print("-"*90+"[Clear]"+"-"*90) ################################################################## Clear
numeros.clear()
print(numeros)
numeros = [1,2,3,4]
numeros= []
print(numeros)

print("-"*90+"[Extend]"+"-"*90) ################################################################## Extend
numeros = [1,2,3,4]
numeros.extend(valores)
print(numeros)

print("-"*90+"[Insert]"+"-"*90) ################################################################# Insert
numeros.insert(3,"en pos 4 agrego esto.")
print(numeros)

print("-"*90+"[Reverse]"+"-"*90) ################################################################# Reverse
numeros.reverse()
print(numeros)

print("-"*90+"[Sort]"+"-"*90) ################################################################# Sort

numeros.pop(-4) #borro el string..
numeros.sort()
print(numeros)



