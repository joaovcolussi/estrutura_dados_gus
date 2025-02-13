# lista = [1,2,3,4]
# lista.append([5,6])
# print(lista)


# lista = [1,2,3,4]
# lista += [5,6]
# print(lista)

# lista = ["João", "Guilherme", "Maria", "Adamastor", "Joelma"]
# lista_pop = lista[:] #Faz cópia da lista
# elemento = lista_pop.pop()
# print(elemento, lista_pop)

# elemento = lista_pop.pop(1)
# print(elemento,lista_pop)

# lista = ["A", "A", "B", "D", "E", "A", "C", "C", "A", "D"]
# lista.remove("D")
# print(lista)


# #List normal
# multiplos = []
# for numero in range(10):
#   multiplos.append(numero * 2)
# print(multiplos)

# #List comprehension
# multiplos = [numero * 2 for numero in range(10)]
# print(multiplos)


# pares = []
# for numero in range(10):
#   if numero % 2 == 0:
#     pares.append(numero)

# pares = [numero for numero in range(10) if numero % 2 ==0]
# print(pares)

# numeros =["par" if numero % 2 ==0 else "impar" for numero in range(10)]
# print(numeros)


# x = 5
# print(id(x))
# x = 7
# print(id(x))

# nome = "Barbabé"
# print(id(nome))

# nome += "Cristiano"
# print(id(nome))


# filme = ["Pulp", "Bastards Inglorious", "Django Livre"]
# print(id(filme))
# filme.append("In Hateful Eight")
# print(id(filme))

def somar (a, b):
  return a + b;

print(somar(4,3))